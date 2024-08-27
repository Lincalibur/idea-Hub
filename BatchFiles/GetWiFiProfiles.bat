@echo off
setlocal

:: Define the output file
set OUTPUT_FILE=WiFi_Profiles.txt

:: Start gathering Wi-Fi profile details
echo ============================================== > %OUTPUT_FILE%
echo Wi-Fi Profiles Report > %OUTPUT_FILE%
echo ============================================== >> %OUTPUT_FILE%

:: Get the list of Wi-Fi profiles
echo Retrieving Wi-Fi profiles... >> %OUTPUT_FILE%
netsh wlan show profiles >> %OUTPUT_FILE%

echo Wi-Fi profiles have been saved to %OUTPUT_FILE%.
pause
