@echo off
setlocal

:: Define paths to the scripts in the same directory
set "GET_PROFILES_SCRIPT=GetWiFiProfiles.bat"
set "GET_PASSWORDS_SCRIPT=GetWiFiPasswords.bat"
set "SETUP_SCRIPT=SetupNewComputer.bat"

:: Function to display a menu
:ShowMenu
cls
echo ==============================================
echo         Interactive Setup Script
echo ==============================================
echo 1. Get Wi-Fi Profiles
echo 2. Get Wi-Fi Passwords
echo 3. Start Setup Process
echo 4. Exit
echo ==============================================
set /p choice="Please select an option (1-4): "

:: Process user choice
if "%choice%"=="1" call "%GET_PROFILES_SCRIPT%"
if "%choice%"=="2" call "%GET_PASSWORDS_SCRIPT%"
if "%choice%"=="3" call "%SETUP_SCRIPT%"
if "%choice%"=="4" exit /b
goto :ShowMenu


:GetWiFiProfiles
:: Call the script to get Wi-Fi profiles
call GetWiFiProfiles.bat
goto :ShowMenu

:GetWiFiPasswords
:: Check if the profiles file exists
if not exist WiFi_Profiles.txt (
    echo WiFi_Profiles.txt does not exist. Please run "Get Wi-Fi Profiles" first.
    pause
    goto :ShowMenu
)

:: Call the script to get Wi-Fi passwords
call GetWiFiPasswords.bat
goto :ShowMenu

:StartSetup
:: Call the setup script
call SetupNewComputer.bat
goto :ShowMenu
