# Deploy all sub-app favicons to CT 101 (10.0.0.212)
$HostIp = "10.0.0.212"
$User = "root"
$BaseLocal = "C:\Projects\Personal Projects"

Write-Host ">>> Starting Sub-App Favicon Deployment to $HostIp <<<" -ForegroundColor Cyan

# 1. Swarovski Collection
Write-Host "Deploying Swarovski Collection..."
scp -B -o BatchMode=yes "$BaseLocal\Swarovski-Collection\public\favicon.svg" "$BaseLocal\Swarovski-Collection\public\favicon.ico" "${User}@${HostIp}:/srv/apps/swarovski-collection/public/"

# 2. Barclays Transactions
Write-Host "Deploying Barclays Transactions..."
scp -B -o BatchMode=yes "$BaseLocal\barclays-transactions\public\favicon.svg" "$BaseLocal\barclays-transactions\public\favicon.ico" "${User}@${HostIp}:/srv/apps/barclays-transactions/public/"

# 3. Maha C9000
Write-Host "Deploying Maha C9000..."
scp -B -o BatchMode=yes "$BaseLocal\Maha-C9000-Battery-Charger-Help\public\favicon.svg" "$BaseLocal\Maha-C9000-Battery-Charger-Help\public\favicon.ico" "${User}@${HostIp}:/srv/apps/maha-c9000-battery-charger/public/"

# 4. Gousto Recipe Search
Write-Host "Deploying Gousto Recipe Search..."
scp -B -o BatchMode=yes "$BaseLocal\Gousto-Recipe-Search\favicon.svg" "$BaseLocal\Gousto-Recipe-Search\favicon.ico" "${User}@${HostIp}:/srv/apps/gousto-recipe-search/"

# 5. EV Charging Cost Calculator
Write-Host "Deploying EV Calculator..."
scp -B -o BatchMode=yes "$BaseLocal\EV-Charging-Cost-Calculator\public\favicon.svg" "$BaseLocal\EV-Charging-Cost-Calculator\public\favicon.ico" "${User}@${HostIp}:/srv/apps/ev-charging-cost-calculator/dist/"

# 6. Movie & TV Database
Write-Host "Deploying Movie & TV Database..."
scp -B -o BatchMode=yes "$BaseLocal\movie-and-tv-database\public\favicon.svg" "$BaseLocal\movie-and-tv-database\public\favicon.ico" "${User}@${HostIp}:/srv/apps/movie-and-tv-database/dist/"

# 7. Music Database
Write-Host "Deploying Music Database..."
scp -B -o BatchMode=yes "$BaseLocal\music-database\public\favicon.svg" "$BaseLocal\music-database\public\favicon.ico" "${User}@${HostIp}:/srv/apps/music-database/public/"

Write-Host "All favicon files successfully copied." -ForegroundColor Green
