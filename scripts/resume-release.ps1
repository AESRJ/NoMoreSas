$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$env:PATH='C:\Program Files\nodejs;C:\Program Files\Git\cmd;'+$env:APPDATA+'\npm;'+$env:PATH
Set-Location -LiteralPath $root
& python (Join-Path $PSScriptRoot 'resume_release.py')
exit $LASTEXITCODE
