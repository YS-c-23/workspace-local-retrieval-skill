$ErrorActionPreference = 'Stop'

function Test-Command($name) {
  return [bool](Get-Command $name -ErrorAction SilentlyContinue)
}

if (-not (Test-Command winget)) {
  Write-Error "winget is required for this helper. Install App Installer / winget first."
}

$packages = @(
  @{ Id = 'Python.Python.3.12'; Label = 'Python 3.12+' },
  @{ Id = 'OpenJS.NodeJS'; Label = 'Node.js' },
  @{ Id = 'SQLite.SQLite'; Label = 'SQLite' }
)

foreach ($pkg in $packages) {
  Write-Host "Installing $($pkg.Label) via winget..."
  winget install --id $pkg.Id --exact --accept-package-agreements --accept-source-agreements --silent
}

Write-Host ""
Write-Host "Prerequisite helper finished."
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Re-run: python scripts/check_retrieval_prereqs.py"
Write-Host "  2. Bootstrap config:"
Write-Host "       python scripts/bootstrap_workspace_retrieval.py --dest .\\retrieval --workspace-root $PWD"
Write-Host "  3. Run the minimal demo:"
Write-Host "       bash scripts/setup_demo.sh"
Write-Host ""
Write-Host "Optional: install Ollama if you want a local embedding backend for semantic retrieval."
