$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
Push-Location $repoRoot
try {
    if (-not (Test-Path -LiteralPath '.venv\Scripts\python.exe')) {
        & python -m venv .venv
        if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear .venv' }
    }
    & .\.venv\Scripts\python.exe -m pip install -r requirements-tools.txt
    if ($LASTEXITCODE -ne 0) { throw 'No se pudieron instalar las herramientas' }
    Write-Host 'Herramientas instaladas. Los archivos de Spec Kit ya estan versionados.'
    Write-Host 'No se reinicializa Spec Kit: evitar sobrescribir las reglas del proyecto.'
} finally { Pop-Location }
