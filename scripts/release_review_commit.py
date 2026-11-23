"""Solo commitea una instantánea aceptada explícitamente por Codex."""
import argparse,json,os,subprocess,time
from pathlib import Path
from datetime import datetime,timezone

root=Path(__file__).resolve().parents[1];repo=Path('C:/Users/Roel/Documents/NoMoreSaaS_Frontend')
p=argparse.ArgumentParser();p.add_argument('feature');p.add_argument('task');p.add_argument('--prepare',action='store_true');p.add_argument('--wait',action='store_true');a=p.parse_args()
assert a.feature in ['005-ajustes-ui','006-acceso-google','007-equipo-y-plan-seguro','008-preparacion-railway']
assert len(a.task)==4 and a.task.startswith('T') and a.task[1:].isdigit()
env=os.environ.copy();env.update(GIT_AUTHOR_NAME='AESRJ',GIT_AUTHOR_EMAIL='vasquez.jorge@uabc.edu.mx',GIT_COMMITTER_NAME='AESRJ',GIT_COMMITTER_EMAIL='vasquez.jorge@uabc.edu.mx')
for k in ['GIT_AUTHOR_DATE','GIT_COMMITTER_DATE']:env.pop(k,None)
def git(*args,input=None):return subprocess.check_output(['git',*args],cwd=repo,env=env,input=input,text=True,encoding='utf-8').strip()
review_path=root/'.local/release-reviews'/f'{a.feature}-{a.task}.json'
review=json.loads(review_path.read_text(encoding='utf-8'))
assert review['reviewer']=='codex' and review['accepted'] is True and review['feature']==a.feature and review['task']==a.task
assert review['verification'] and review['paths'] and review['title'] and review['body']
assert 'co-authored-by:' not in review['body'].lower(),'Sin coautoría automática'
assert git('branch','--show-current')=='feat/revision-y-railway'
pending=root/'.local/release-pending-commit.json';ledger=root/'.local/release-commits.json'
records=json.loads(ledger.read_text(encoding='utf-8')) if ledger.exists() else []
if pending.exists():
 frozen=json.loads(pending.read_text(encoding='utf-8'));assert frozen['feature']==a.feature and frozen['task']==a.task,'Otra instantánea pendiente'
else:
 assert not git('diff','--cached','--name-only'),'Índice previo ocupado: no mezclar cambios'
 assert git('rev-parse','HEAD')==review['base_commit'],'Base distinta de revisión'
 for rel in review['paths']:
  resolved=(repo/rel).resolve();assert resolved.is_relative_to(repo.resolve())
  assert '.env' not in resolved.parts and '.local' not in Path(rel).parts and Path(rel).suffix not in ['.sqlite','.db']
 # Optional immutable blobs preserve an accepted task while later reviewed work
 # continues in the working tree. Only explicitly reviewed paths are staged.
 blobs=review.get('reviewed_blobs')
 if blobs is not None:
  assert set(blobs)==set(review['paths']),'Los blobs deben corresponder exactamente a los paths revisados'
  for rel,entry in blobs.items():
   oid=entry['oid'];mode=entry['mode']
   assert len(oid)==40 and all(c in '0123456789abcdef' for c in oid),'OID invalido'
   assert mode in ['100644','100755'],'Modo no permitido'
   assert git('cat-file','-t',oid)=='blob','Objeto revisado no es blob'
  for rel,entry in blobs.items():
   oid=entry['oid'];mode=entry['mode']
   git('update-index','--add','--cacheinfo',mode+','+oid+','+rel)
 else:
  git('add','--',*review['paths'])
 if review.get('history_sections'):
  rel='.project/progress/history.md';before=git('show','HEAD:'+rel)+'\n';current=(repo/rel).read_text(encoding='utf-8')
  for section in review['history_sections']:
   assert section.strip() and section in current and section.strip() not in before,'Entrada de historia no revisada o duplicada'
   before+='\n'+section.strip()+'\n'
  oid=git('hash-object','-w','--stdin',input=before);git('update-index','--cacheinfo','100644,'+oid+','+rel)
 assert git('diff','--cached','--name-only'),'Sin cambios revisados'
 frozen={'feature':a.feature,'task':a.task,'base':git('rev-parse','HEAD'),'tree':git('write-tree'),'title':review['title'],'body':review['body'],'verification':review['verification']}
 pending.write_text(json.dumps(frozen,ensure_ascii=False,indent=2),encoding='utf-8')
if a.prepare:print('PREPARED_REVIEWED_SNAPSHOT');raise SystemExit(0)
if records:
 previous=datetime.fromisoformat(records[-1]['committed_at'])
else:
 previous=datetime.fromtimestamp(int(git('log','-1','--format=%ct')),timezone.utc)
while True:
 remaining=1200-(datetime.now(timezone.utc)-previous).total_seconds()
 if remaining<=0:break
 if not a.wait:print(f'WAIT_COMMIT_WINDOW_SECONDS={int(remaining)+1}; snapshot stays frozen');raise SystemExit(2)
 # Ejecutar --wait en proceso de fondo oculto, no bloquear la conversación.
 time.sleep(min(30,remaining))
assert git('rev-parse','HEAD')==frozen['base'] and git('write-tree')==frozen['tree'],'Índice/base cambiaron tras revisión; no hacer commit'
git('commit','-m',frozen['title'],'-m',frozen['body'])
record={'feature':a.feature,'task':a.task,'commit':git('rev-parse','HEAD'),'committed_at':datetime.now(timezone.utc).isoformat(),'verification':frozen['verification']}
records.append(record);ledger.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');pending.unlink()
print(json.dumps(record,ensure_ascii=False))
