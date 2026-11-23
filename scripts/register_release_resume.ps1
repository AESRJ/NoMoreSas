param([datetimeoffset]$NotBefore='2026-11-22T14:21:00-08:00')
$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$configPath=Join-Path $root '.local/release-resume-config.json'
$config=Get-Content -LiteralPath $configPath -Raw -Encoding utf8|ConvertFrom-Json
if(-not $config.enabled){throw 'Reanudación desactivada'}
if($NotBefore -le [datetimeoffset]::Now){throw 'Horario pasado: revisar cuota y programar un horario explícito nuevo'}
$taskName='NoMoreSaaS-Reanudar-'+$NotBefore.ToString('yyyyMMdd-HHmm')
$expected=Join-Path $PSScriptRoot 'resume-release.ps1'
$registration=@{method=$null;task_name=$taskName;not_before=$NotBefore.ToString('o');verified=$false}
try{
 $existing=Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
 if($existing){throw 'Ya existe tarea con ese nombre; no sustituirla sin revisión'}
 $execute=Join-Path $env:SystemRoot 'System32/WindowsPowerShell/v1.0/powershell.exe'
 $arguments='-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File "'+$expected+'"'
 $action=New-ScheduledTaskAction -Execute $execute -Argument $arguments -WorkingDirectory $root
 $trigger=New-ScheduledTaskTrigger -Once -At $NotBefore.LocalDateTime
 $principal=New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
 $settings=New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew -ExecutionTimeLimit ([TimeSpan]::FromHours(8))
 [void](Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description 'NoMoreSaaS: Codex coordina/revisa, Claude construye; reintento tras cuota. Sin compras/push por inferencia.')
 $registered=Get-ScheduledTask -TaskName $taskName
 $info=Get-ScheduledTaskInfo -TaskName $taskName
 if($registered.Actions[0].Arguments -ne $arguments){throw 'Acción programada distinta a la preparada'}
 $registration.method='windows_scheduled_task';$registration.verified=$true;$registration.next_run_time=$info.NextRunTime.ToString('o');$registration.state=$registered.State.ToString()
}catch{
 # No elevar privilegios ni modificar políticas. Un temporizador de usuario es una alternativa menos persistente.
 $registration.scheduler_error=$_.Exception.Message
 $existing=Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
 if($existing){throw 'Existe tarea después del error; revisar antes de iniciar otra vía'}
 $python=(Get-Command python -ErrorAction Stop).Source
 $timer=Join-Path $PSScriptRoot 'resume_release_timer.py'
 $process=Start-Process -FilePath $python -ArgumentList ('"'+$timer+'"') -WorkingDirectory $root -WindowStyle Hidden -PassThru
 Start-Sleep -Seconds 2
 if($process.HasExited){throw 'Temporizador de respaldo terminó antes de quedar listo'}
 $timerState=Get-Content -LiteralPath (Join-Path $root '.local/release-timer-state.json') -Raw -Encoding utf8|ConvertFrom-Json
 if($timerState.status -ne 'waiting'){throw 'Temporizador no quedó en espera'}
 $registration.method='hidden_user_timer';$registration.pid=$process.Id;$registration.verified=$true;$registration.state='waiting';$registration.persistence='Solo mientras el equipo/sesión/proceso permanezcan disponibles; no sobrevive a reinicio'
}
$registration|ConvertTo-Json -Depth 5|Set-Content -LiteralPath (Join-Path $root '.local/release-schedule-registration.json') -Encoding utf8
$registration|ConvertTo-Json -Compress -Depth 5
