"""Temporizador de usuario de respaldo si Windows no permite registrar una tarea."""
import json,subprocess,sys,time,os
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1];config=root/'.local/release-resume-config.json';state=root/'.local/release-timer-state.json'
def record(status):state.write_text(json.dumps({'status':status,'pid':os.getpid(),'updated_at':datetime.now(timezone.utc).isoformat()},indent=2)+'\n',encoding='utf-8')
record('waiting')
while True:
 data=json.loads(config.read_text(encoding='utf-8'))
 if not data.get('enabled'):record('cancelled');break
 remaining=(datetime.fromisoformat(data['not_before'])-datetime.now(timezone.utc)).total_seconds()
 if remaining<=0:
  record('starting_coordinator')
  result=subprocess.run([sys.executable,str(root/'scripts/resume_release.py')],cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  record('coordinator_returned_'+str(result.returncode));break
 time.sleep(min(15,remaining))
