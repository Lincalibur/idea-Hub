@echo off
setlocal

:: Define the path to the Wi-Fi credentials file
set CREDENTIALS_FILE=WiFi_Credentials.txt

:: Check if the script is running as administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

echo ==============================================
echo Starting New Computer Setup...
echo ==============================================

:: Step 1: Extract SSID and Password from the Credentials File
echo Extracting SSID and Password...
for /f "tokens=1,2,* delims=:" %%a in ('findstr /C:"Key Content" %CREDENTIALS_FILE%') do (
    set KEY=%%c
    set KEY=!KEY:~1!
    set PROFILE_NAME=%%a
    set PROFILE_NAME=!PROFILE_NAME:~1!
)

:: Connect to Wi-Fi
echo Connecting to Wi-Fi: !PROFILE_NAME! with Password: !KEY!
netsh wlan add profile filename="wifi_profile.xml"
netsh wlan connect name="%PROFILE_NAME%" ssid="%PROFILE_NAME%" key="%KEY%"
echo Connected to Wi-Fi!

:: Step 2: Install Required Applications

:: Install Brave Browser
echo Checking if Brave Browser is installed...
reg query "HKCU\Software\BraveSoftware\Brave-Browser" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Brave Browser...
    start /wait msiexec /i "https://laptop-updates.brave.com/latest/winx64" /quiet /norestart
) else (
    echo Brave Browser is already installed.
)

:: Install VLC Media Player
echo Checking if VLC Media Player is installed...
reg query "HKCU\Software\VideoLAN\VLC" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing VLC Media Player...
    start /wait msiexec /i "https://get.videolan.org/vlc/last/win64/vlc-3.0.16-win64.msi" /quiet /norestart
) else (
    echo VLC Media Player is already installed.
)

:: Install 7-Zip
echo Checking if 7-Zip is installed...
reg query "HKCU\Software\7-Zip" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing 7-Zip...
    start /wait msiexec /i "https://www.7-zip.org/a/7z1900-x64.msi" /quiet /norestart
) else (
    echo 7-Zip is already installed.
)

:: Install Notepad++
echo Checking if Notepad++ is installed...
reg query "HKCU\Software\Notepad++" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Notepad++...
    start /wait msiexec /i "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/latest/download/npp.8.1.9.Installer.x64.exe" /quiet /norestart
) else (
    echo Notepad++ is already installed.
)

:: Set Brave as Default Browser
echo Setting Brave as the default browser...
reg query "HKCU\Software\BraveSoftware\Brave-Browser" >nul 2>&1
if %errorlevel% neq 0 (
    echo Brave is not installed. Please install Brave manually.
) else (
    echo Setting Brave as the default browser...
    powershell -Command "Start-Process 'ms-settings:defaultapps' -ArgumentList 'defaultapps' -Wait"
    timeout /t 5
    echo Brave set as the default browser.
)

:: Step 3: Check for Windows Updates
echo Checking for Windows Updates...
powershell -Command "Get-WindowsUpdate | Out-Null"
if %errorlevel% neq 0 (
    echo Installing Windows Updates...
    powershell -Command "Install-WindowsUpdate -AcceptAll -AutoReboot"
) else (
    echo Your system is up to date.
)

echo ==============================================
echo New Computer Setup Complete!
echo ==============================================
pause
