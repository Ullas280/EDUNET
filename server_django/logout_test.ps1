$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession

$loginBody = @{
  email='testuser+3@example.com'
  password='TestPass123'
  role='student'
} | ConvertTo-Json

Write-Output '--- Login ---'
try {
  $responseLogin = Invoke-RestMethod -Uri 'http://localhost:8000/api/v1/user/login' -Method POST -Body $loginBody -ContentType 'application/json' -WebSession $session
  $responseLogin | ConvertTo-Json -Compress | Write-Output
} catch {
  Write-Output 'LOGIN ERROR:'
  $_ | Format-List * -Force
}

Write-Output '--- Cookies after login ---'
$session.Cookies.GetCookies('http://localhost:8000') | ForEach-Object { Write-Output ($_.Name + '=' + $_.Value) }

Write-Output '--- Logout ---'
try {
  $responseLogout = Invoke-RestMethod -Uri 'http://localhost:8000/api/v1/user/logout' -Method POST -Body '{}' -ContentType 'application/json' -WebSession $session
  $responseLogout | ConvertTo-Json -Compress | Write-Output
} catch {
  Write-Output 'LOGOUT ERROR:'
  $_ | Format-List * -Force
}

Write-Output '--- Cookies after logout ---'
$session.Cookies.GetCookies('http://localhost:8000') | ForEach-Object { Write-Output ($_.Name + '=' + $_.Value) }
