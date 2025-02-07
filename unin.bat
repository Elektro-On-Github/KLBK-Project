del "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\*.exe*"
echo Ripristino di Windows Defender in corso… 
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
wpeutil reboot