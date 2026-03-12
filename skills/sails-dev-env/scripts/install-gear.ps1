param(
    [string]$Tag = "",
    [string]$Target = "x86_64-pc-windows-msvc",
    [string]$Destination = "$env:USERPROFILE\AppData\Local\Programs\gear\bin"
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Tag)) {
    $release = Invoke-RestMethod -Uri "https://api.github.com/repos/gear-tech/gear/releases/latest"
    $Tag = $release.tag_name
}

$archiveName = "gear-$Tag-$Target.zip"
$archiveUrl = "https://get.gear.rs/$archiveName"
$tmpDir = Join-Path $env:TEMP ("gear-" + [guid]::NewGuid().ToString())
$archivePath = Join-Path $tmpDir $archiveName

New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null
New-Item -ItemType Directory -Force -Path $Destination | Out-Null

try {
    Invoke-WebRequest -Uri $archiveUrl -OutFile $archivePath
    Expand-Archive -LiteralPath $archivePath -DestinationPath $tmpDir -Force
    Get-ChildItem -Path $tmpDir -Filter "gear*.exe" -Recurse | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Destination -Force
    }
}
finally {
    if (Test-Path $tmpDir) {
        Remove-Item -LiteralPath $tmpDir -Recurse -Force
    }
}

Write-Host "Installed Gear release $Tag to $Destination"
