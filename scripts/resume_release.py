"""Reanuda el coordinador Codex; Claude sigue siendo el único constructor."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,shutil,subprocess,threading

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/'.local/release-resume-config.json'
STATE=ROOT/'.local/release-resume-state.json'
LOCK=ROOT/'.local/release-running.lock'
def save(state):
 state['updated_at']=datetime.now(timezone.utc).isoformat()
 STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo,text=True,encoding='utf-8').strip()
def preflight(config):
 repo=Path(config['code_repository']).resolve()
 assert config['enabled'] is True,'Reanudación desactivada'
 assert repo==Path('C:/Users/Roel/Documents/NoMoreSaaS_Frontend').resolve()
 assert git(repo,'rev-parse','HEAD')==config['expected_code_head'],'HEAD cambió desde preparación: revisar antes de construir'
 assert git(repo,'branch','--show-current')=='feat/revision-y-railway','Rama no preparada'
 assert not git(repo,'diff','--cached','--name-only'),'Índice ocupado; no mezclar trabajo'
 current=git(repo,'status','--porcelain','--untracked-files=all')
 assert current==config['baseline_status'],'Worktree cambió desde preparación; preservar cambios y revisar'
 for rel,digest in config['baseline_hashes'].items():
  path=(repo/rel).resolve();assert path.is_relative_to(repo)
  assert path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==digest,'Archivo previo cambió: '+rel
 queue=json.loads((repo/'.project/execution-queue.json').read_text(encoding='utf-8'))
 active=config.get('expected_active_feature','005-ajustes-ui')
 assert active in queue['order'] and queue['active']==active,'Entrega activa distinta a la preparada'
 handoff=json.loads((repo/'.project/handoffs'/f'{active}.json').read_text(encoding='utf-8'))
 assert handoff['status']=='ready' and not handoff['blockers']
 return repo

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--smoke',action='store_true');a=p.parse_args()
 env=os.environ.copy();env['PATH']='C:/Program Files/nodejs;C:/Program Files/Git/cmd;'+str(Path(env.get('APPDATA',''))/'npm')+';'+env.get('PATH','')
 # Usar la autenticación ChatGPT comprobada, sin activar facturación API por entorno heredado.
 env.pop('OPENAI_API_KEY',None);env.pop('CODEX_API_KEY',None)
 codex=shutil.which('codex',path=env['PATH']);assert codex,'Codex CLI no encontrado'
 if a.smoke:
  out=ROOT/'.local/codex-resume-smoke-native.txt'
  cmd=[codex,'exec','--sandbox','read-only','-c','approval_policy="never"','--color','never','--output-last-message',str(out),'-']
  result=subprocess.run(cmd,input='Reply exactly HARNESS_OK. Do not call tools or inspect files.',cwd=ROOT,env=env,text=True,encoding='utf-8',stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=90)
  assert result.returncode==0 and out.read_text(encoding='utf-8').strip()=='HARNESS_OK',f'Smoke Codex falló, exit={result.returncode}'
  print('CODEX_COORDINATOR_NATIVE_SMOKE_OK');return
 config=json.loads(CONFIG.read_text(encoding='utf-8'));repo=preflight(config)
 if a.check:print('RESUME_PREFLIGHT_OK: rama, HEAD, índice, cambios previos y entrega activa');return
 due=datetime.fromisoformat(config['not_before'])
 if datetime.now(timezone.utc)<due:save({'status':'waiting_scheduled_time','not_before':config['not_before']});return
 try:handle=LOCK.open('x',encoding='utf-8')
 except FileExistsError:save({'status':'already_running_or_stale_lock','lock':str(LOCK)});return
 with handle:handle.write(json.dumps({'pid':os.getpid(),'started_at':datetime.now(timezone.utc).isoformat()}))
 try:
  report=ROOT/'.local/release-coordinator-report.md';events=ROOT/'.local/release-coordinator-events.jsonl'
  prompt=(ROOT/'handoffs/release-coordinator.md').read_text(encoding='utf-8')
  recovery=config.get('recovery_note')
  if recovery:
   note=(ROOT/recovery).resolve();assert note.is_relative_to(ROOT/'.local')
   prompt+='\n\nESTADO DE RECUPERACIÓN VERIFICADO POR CODEX:\n'+note.read_text(encoding='utf-8')
  cmd=[codex,'exec','--sandbox','danger-full-access','-c','approval_policy="never"','--add-dir',str(repo),'--json','--output-last-message',str(report),'-']
  state={'status':'running','pid':os.getpid(),'code_head_at_start':config['expected_code_head'],'report':str(report),'event_count':0};save(state)
  child=subprocess.Popen(cmd,cwd=ROOT,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,encoding='utf-8',errors='replace',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  cancelled=threading.Event();finished=threading.Event()
  def watch_cancel():
   while not finished.wait(5):
    try:enabled=json.loads(CONFIG.read_text(encoding='utf-8')).get('enabled') is True
    except (OSError,ValueError):continue
    if not enabled and child.poll() is None:
     cancelled.set()
     # PID de nuestro propio hijo vivo: detener solo su árbol de procesos.
     if os.name=='nt':subprocess.run(['taskkill','/PID',str(child.pid),'/T','/F'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=False)
     else:child.terminate()
     return
  threading.Thread(target=watch_cancel,daemon=True).start()
  child.stdin.write(prompt);child.stdin.close()
  with events.open('a',encoding='utf-8') as log:
   for line in child.stdout:
    try:row=json.loads(line)
    except ValueError:continue
    item=row.get('item',{})
    if row.get('type') in ['error','turn.failed']:
     # Clasificar sin persistir mensajes, argumentos ni contenido sensible.
     error=str(row.get('message',''))+' '+str(row.get('error',''))
     lower=error.lower()
     state['failure_category']='quota_or_billing' if any(s in lower for s in ['usage limit','rate limit','quota','credits','billing']) else ('context_limit' if any(s in lower for s in ['context window','context length']) else ('connection' if any(s in lower for s in ['stream disconnected','connection','network','timed out']) else 'unclassified'))
    # No guardar razonamiento, prompts, argumentos ni salidas crudas de herramientas.
    lean={'time':datetime.now(timezone.utc).isoformat(),'event':row.get('type'),'item_type':item.get('type'),'status':item.get('status'),'exit_code':item.get('exit_code')}
    if row.get('type')=='thread.started':lean['thread_id']=row.get('thread_id')
    if row.get('type') in ['thread.started','turn.started','turn.completed','turn.failed','error','item.completed']:
     if item.get('type') not in ['reasoning','agent_message']:
      log.write(json.dumps(lean,ensure_ascii=False)+'\n');log.flush();state['event_count']+=1;save(state)
  exit_code=child.wait();finished.set();state.update(status='cancelled' if cancelled.is_set() else ('finished' if exit_code==0 else 'failed'),exit_code=exit_code)
  index=json.loads((ROOT/'feature_list.json').read_text(encoding='utf-8'))
  ids={'UX-REVISION','AUTH-GOOGLE','MVP-EQUIPO-ASISTIDO','DEPLOY-RAILWAY'}
  statuses={f['id']:f['status'] for f in index['features'] if f['id'] in ids};state['features']=statuses
  if exit_code==0 and any(value!='done' for value in statuses.values()):state['status']='needs_review_or_external_setup'
  save(state)
 finally:
  # Solo eliminar el lock creado por este proceso; nunca rutas calculadas fuera del arnés.
  if LOCK.is_file():
   own=json.loads(LOCK.read_text(encoding='utf-8'))
   if own.get('pid')==os.getpid():LOCK.unlink()

if __name__=='__main__':
 try:main()
 except Exception as error:
  save({'status':'preflight_or_runtime_blocked','message':str(error)})
  raise
