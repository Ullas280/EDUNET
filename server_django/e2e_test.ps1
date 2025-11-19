$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession

$regBody = @{
  fullname='Test User 3'
  email='testuser+3@example.com'
  phoneNumber='1234567890'
  password='TestPass123'
  role='student'
} | ConvertTo-Json

Write-Output '--- Register ---'
try {
  $responseReg = Invoke-RestMethod -Uri 'http://localhost:8000/api/v1/user/register' -Method POST -Body $regBody -ContentType 'application/json' -WebSession $session
  $responseReg | ConvertTo-Json -Compress | Write-Output
  Write-Output "User Created: $($responseReg.user.fullname) ($($responseReg.user.email)) - Role: $($responseReg.user.role)"
} catch {
  Write-Output 'REGISTER ERROR:'
  $_ | Format-List * -Force
}

Write-Output '--- Login ---'
$loginBody = @{
  email='testuser+3@example.com'
  password='TestPass123'
  role='student'
} | ConvertTo-Json

try {
  $responseLogin = Invoke-RestMethod -Uri 'http://localhost:8000/api/v1/user/login' -Method POST -Body $loginBody -ContentType 'application/json' -WebSession $session
  $responseLogin | ConvertTo-Json -Compress | Write-Output
  Write-Output "Logged in as: $($responseLogin.user.fullname)"
} catch {
  Write-Output 'LOGIN ERROR:'
  $_ | Format-List * -Force
}

Write-Output '--- Cookies ---'
$session.Cookies.GetCookies('http://localhost:8000') | ForEach-Object { Write-Output ($_.Name + '=' + $_.Value) }
