$ErrorActionPreference = "Stop"

$installer = Join-Path $PSScriptRoot "scripts\install.py"

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $installer @args
    exit $LASTEXITCODE
}

if (Get-Command python -ErrorAction SilentlyContinue) {
    & python $installer @args
    exit $LASTEXITCODE
}

if (Get-Command python3 -ErrorAction SilentlyContinue) {
    & python3 $installer @args
    exit $LASTEXITCODE
}

Write-Error "Python 3 is required to install My Agent."
exit 1
