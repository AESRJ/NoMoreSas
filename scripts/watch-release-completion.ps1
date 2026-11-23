$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$statePath=Join-Path $root '.local/release-resume-state.json'
$noticePath=Join-Path $root '.local/release-finish-notifier.json'
$sessionId=[Diagnostics.Process]::GetCurrentProcess().SessionId
$messenger=Join-Path $env:SystemRoot 'System32/msg.exe'
$terminal=@('finished','needs_review_or_external_setup','failed','cancelled','preflight_or_runtime_blocked')
function Save-Notice([string]$status, $extra=@{}) {
 $entry=@{status=$status;pid=$PID;updated_at=[DateTimeOffset]::Now.ToString('o');poll_seconds=30}
 foreach($key in $extra.Keys){$entry[$key]=$extra[$key]}
 $entry|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $noticePath -Encoding utf8
}
if(Test-Path -LiteralPath $noticePath){
 $previous=Get-Content -LiteralPath $noticePath -Raw -Encoding utf8|ConvertFrom-Json
 if($previous.status -eq 'watching' -and (Get-Process -Id $previous.pid -ErrorAction SilentlyContinue)){throw 'Ya hay un observador de finalizacion activo'}
}
Save-Notice 'watching'
while($true){
 try{$state=Get-Content -LiteralPath $statePath -Raw -Encoding utf8|ConvertFrom-Json}catch{Start-Sleep -Seconds 30;continue}
 if($state.status -in $terminal){
  $features=@($state.features.PSObject.Properties)
  $complete=$state.status -eq 'finished' -and $features.Count -eq 4 -and @($features|Where-Object {$_.Value -ne 'done'}).Count -eq 0
  $message=if($complete){'NoMoreSaaS: el flujo completo termino. Consulta el reporte final en ProyectoWeb/.local/release-coordinator-report.md.'}else{'NoMoreSaaS: la ejecucion termino con pendientes o un bloqueo. Consulta ProyectoWeb/progress/current.md y .local/release-coordinator-report.md.'}
  # Avisar solamente a esta sesion local, nunca a otras cuentas ni servicios externos.
  & $messenger "$sessionId" '/TIME:120' $message
  $notificationExit=$LASTEXITCODE
  Save-Notice $(if($notificationExit -eq 0){'notification_sent'}else{'notification_failed'}) @{execution_status=$state.status;all_features_done=$complete;notification_exit=$notificationExit}
  break
 }
 Start-Sleep -Seconds 30
}
