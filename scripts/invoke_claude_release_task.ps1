param(
 [ValidatePattern('^00[5-8]-[a-z0-9-]+$')][string]$Feature='005-ajustes-ui',
 [ValidatePattern('^T[0-9]{3}$')][string]$TaskId='T001',
 [string]$RepairNote=''
)
$ErrorActionPreference='Stop'
$master=Split-Path -Parent $PSScriptRoot
$repo='C:\Users\Roel\Documents\NoMoreSaaS_Frontend'
$env:PATH='C:\Program Files\nodejs;C:\Program Files\Git\cmd;'+$env:APPDATA+'\npm;'+$env:PATH
$env:CLAUDE_CODE_GIT_BASH_PATH='C:\Program Files\Git\bin\bash.exe'
$env:IMPECCABLE_HOME=Join-Path $repo '.local/impeccable-engine'
$env:SPECIFY_INIT_DIR=$repo
$env:API_PORT='3501';$env:WEB_PORT='5773'
Set-Location -LiteralPath $repo
$handoffPath=".project/handoffs/$Feature.json"
python tools/check_handoff.py --implementation-ready $handoffPath
if($LASTEXITCODE -ne 0){exit 1}
$handoff=Get-Content -LiteralPath $handoffPath -Raw -Encoding utf8|ConvertFrom-Json
if($TaskId -notin $handoff.task_ids){throw 'Tarea no autorizada por entrega'}
$queue=Get-Content -LiteralPath '.project/execution-queue.json' -Raw -Encoding utf8|ConvertFrom-Json
if($queue.active -ne $Feature){throw 'Otra funcionalidad es la activa'}
if((git branch --show-current) -ne $queue.branch){throw 'Rama distinta a la preparada; requiere revisión Codex'}
$tasks=Get-Content -LiteralPath ".project/specs/$Feature/tasks.md" -Raw -Encoding utf8
if(-not $RepairNote -and $tasks -notmatch "(?m)^- \[ \] $TaskId\b"){throw 'Tarea ya marcada o ausente; no repetir sin revisión'}
if($RepairNote){
 $resolved=(Resolve-Path -LiteralPath $RepairNote).Path
 if(-not $resolved.StartsWith((Join-Path $master '.local')+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){throw 'Nota de reparación fuera del área de revisión'}
}
$prompt=@"
Eres Claude Code constructor. Codex planifica/revisa y tú escribes producto. Implementa UNA tarea $TaskId de .project/specs/$Feature/tasks.md con /speckit-implement, bajo entrega $handoffPath ready y sin bloqueos. Lee AGENTS, CLAUDE, constitución, contexto, entrega y artefactos pertinentes. No ejecutar tareas siguientes ni entregas cerradas. No ampliar alcance ni modificar spec/plan/modelo/contratos/handoff/instrucciones para autoautorizarte. Si hay contradicción material, informa evidencia a Codex.

Conservar stack, proyectos/usuarios/DB local y cambios preexistentes. No git add/commit/push/reset/clean/force, desplegar, compras, SSH ni cambios globales de seguridad. Codex revisa/hace commit por tarea, aproximadamente20min, nunca fechas falsas. Puedes marcar solo tu checkbox tras verificar y escribir evidencia breve .project/progress/impl_$($handoff.feature_id).md/history append-only: archivos, comandos/resultados reales y límites, sin razonamiento interno. No cerrar feature ni aprobar tu trabajo.

Mantener aislamiento/CSRF/sesiones/Origin, errores y datos previos, fuentes oficiales y estimaciones honestas. No imprimir .env, tokens o secretos. Google y Railway requieren configuración real antes de afirmar pruebas vivas. No reutilizar credenciales de conectores ni pedir claves en chat. Diagnóstico007 usa fixtures: no recoger inventario real de este ordenador. No ejecutar instalaciones de aplicaciones del catálogo ni escanear redes.

Priorizar trabajo completo revisable y checks por riesgo: pruebas enfocadas por tarea; lint/build/smoke al integrar. No suites completas repetidas sin motivo ni tests espejo. Entorno de prueba heredado3501/5773; ejecuta pnpm sin prefijos de variables ni wrappers cmd con asignaciones. No usar preview3301/5573 ni su DB. Si herramienta requiere aprobación no disponible, informa y sigue solo trabajo independiente, sin simular éxito.

Impeccable existente para UI; conservar paleta y computadora Higgsfield real. Usuario pidió NO documentar mejora ni PRODUCT/DESIGN; no nueva generación/créditos. Node/pnpm locales fijados. CuotaClaude agotada: informa y detente, no cambiar cuenta/modelo ni eludir límite.

Al terminar: resumen concreto, verificaciones y bloqueos; DETENTE tras $TaskId. Codex decide aceptación y siguiente tarea.
"@
if($RepairNote){$prompt+="`nCORRECCIONES CODEX PARA ESTA MISMA TAREA:`n"+(Get-Content -LiteralPath $resolved -Raw -Encoding utf8)}
$exe=Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Packages\Anthropic.ClaudeCode_Microsoft.Winget.Source_8wekyb3d8bbwe\claude.exe'
$allow=@('Read','Glob','Grep','Write','Edit','Skill','WebFetch','WebSearch','Bash(pnpm *)','Bash(pnpm.cmd *)','Bash(node *)','Bash(python tools/check_handoff.py *)','Bash(git status*)','Bash(git diff*)','Bash(git log*)','Bash(ls *)','Bash(cat *)','PowerShell(pnpm *)','PowerShell(node *)','PowerShell(python tools/check_handoff.py *)','PowerShell(init.cmd)','PowerShell(.\init.cmd)','Bash(./init.cmd)') -join ','
if($Feature -eq '008-preparacion-railway'){$allow+=',Bash(docker build*),Bash(docker run*),Bash(docker inspect*),PowerShell(docker build*),PowerShell(docker run*),PowerShell(docker inspect*)'}
$deny=@('Bash(git add*)','Bash(git commit*)','Bash(git push*)','Bash(git reset*)','Bash(git clean*)','PowerShell(git add*)','PowerShell(git commit*)','PowerShell(git push*)','PowerShell(git reset*)','PowerShell(git clean*)') -join ','
$logDir=Join-Path $repo '.local/release-logs';[void](New-Item -ItemType Directory -Path $logDir -Force)
$stamp=Get-Date -Format 'yyyyMMdd-HHmmss'
$log=Join-Path $logDir "$Feature-$TaskId-$stamp.jsonl"
$sessionFile=Join-Path $logDir "$Feature-session.json"
$resume=@()
if(Test-Path -LiteralPath $sessionFile){$saved=Get-Content -LiteralPath $sessionFile -Raw|ConvertFrom-Json;if($saved.session_id){$resume=@('--resume',$saved.session_id)}}
$OutputEncoding=New-Object System.Text.UTF8Encoding($false)
$oldErrorAction=$ErrorActionPreference;$ErrorActionPreference='Continue'
# Filtrar thinking/razonamiento y resultados brutos. La evidencia seleccionada vive en .project/progress.
$prompt|& $exe @resume -p --permission-mode acceptEdits --allowedTools $allow --disallowedTools $deny --output-format stream-json --verbose --prompt-suggestions false 2>$null|ForEach-Object{
 try{
  $row=$_|ConvertFrom-Json
  if($row.type -eq 'system' -and $row.subtype -eq 'init'){
   @{session_id=$row.session_id}|ConvertTo-Json|Set-Content -LiteralPath $sessionFile -Encoding utf8
   @{type='init';session_id=$row.session_id;time=(Get-Date).ToString('o')}|ConvertTo-Json -Compress
  }elseif($row.type -eq 'result'){
   @{type='result';is_error=$row.is_error;result=$row.result;session_id=$row.session_id;time=(Get-Date).ToString('o')}|ConvertTo-Json -Compress -Depth 5
  }elseif($row.type -eq 'assistant'){
   foreach($item in $row.message.content){
    if($item.type -eq 'text'){@{type='message';text=$item.text;time=(Get-Date).ToString('o')}|ConvertTo-Json -Compress -Depth 3}
    elseif($item.type -eq 'tool_use'){@{type='tool';name=$item.name;time=(Get-Date).ToString('o')}|ConvertTo-Json -Compress}
   }
  }
 }catch{ }
}|Out-File -LiteralPath $log -Encoding utf8
$nativeExit=$LASTEXITCODE;$ErrorActionPreference=$oldErrorAction
Write-Output "CLAUDE_EXIT=$nativeExit FEATURE=$Feature TASK=$TaskId LOG=$log"
exit $nativeExit
