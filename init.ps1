$ErrorActionPreference = 'Stop'
$repoRoot = $PSScriptRoot
$pythonPath = Join-Path $repoRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $pythonPath)) { $pythonPath = 'python' }
& $pythonPath (Join-Path $repoRoot 'scripts\check_harness.py')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
foreach ($tool in @('git', 'codex', 'claude')) {
    if (Get-Command $tool -ErrorAction SilentlyContinue) { Write-Host "OK herramienta: $tool" }
    else { Write-Warning "Herramienta pendiente: $tool" }
}
Write-Host 'Arnes verificado. Consulta progress/current.md para continuar.'
