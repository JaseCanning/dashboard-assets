param(
    [string]$HostIp = "10.0.0.212",
    [string]$User = "root",
    [string]$RemotePath = "/srv/apps/dashboard/public"
)

$assetsDir = $PSScriptRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Deploying Favicons to Jason Canning Portal" -ForegroundColor Cyan
Write-Host " Destination: ${User}@${HostIp}:${RemotePath}" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Ensure remote directory exists
Write-Host "`n[1/3] Ensuring remote directory exists..." -ForegroundColor Yellow
ssh -n -o BatchMode=yes "${User}@${HostIp}" "mkdir -p ${RemotePath}"

# 2. Copy favicon assets
Write-Host "[2/3] Copying favicon assets..." -ForegroundColor Yellow
scp -B "$assetsDir\favicon*" "${User}@${HostIp}:${RemotePath}/"
scp -B "$assetsDir\apple-touch-icon.png" "${User}@${HostIp}:${RemotePath}/"
scp -B "$assetsDir\android-chrome-*.png" "${User}@${HostIp}:${RemotePath}/"
scp -B "$assetsDir\site.webmanifest" "${User}@${HostIp}:${RemotePath}/"

# 3. Check status
Write-Host "[3/3] Verifying files on server..." -ForegroundColor Yellow
ssh -n -o BatchMode=yes "${User}@${HostIp}" "ls -la ${RemotePath}/favicon*"

Write-Host "`nFavicon deployment completed successfully!" -ForegroundColor Green
Write-Host "Test live at: https://jasoncanning.uk/favicon.ico and https://jasoncanning.uk/favicon.svg" -ForegroundColor Cyan
