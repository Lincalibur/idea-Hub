@echo off
setlocal enabledelayedexpansion

:: Define input and output files
set INPUT_FILE=WiFi_Profiles.txt
set OUTPUT_FILE=WiFi_Passwords.txt

:: Check if input file exists
if not exist %INPUT_FILE% (
    echo %INPUT_FILE% does not exist. Please run "Get Wi-Fi Profiles" first.
    pause
    exit /b
)

:: Start gathering Wi-Fi profile details
echo ============================================== > %OUTPUT_FILE%
echo Wi-Fi Details Report > %OUTPUT_FILE%
echo ============================================== >> %OUTPUT_FILE%

:: Read each line from the input file
for /f "tokens=1,* delims=:" %%a in (%INPUT_FILE%) do (
    set "LINE=%%b"
    set "LINE=!LINE:~1!"

    :: Skip lines that are not profiles
    if "!LINE!" neq "" (
        echo Retrieving details for: !LINE! >> %OUTPUT_FILE%
        netsh wlan show profile name="!LINE!" key=clear >> %OUTPUT_FILE%
        echo. >> %OUTPUT_FILE%
    )
)

echo Wi-Fi details have been saved to %OUTPUT_FILE%.
pause
