@echo off
echo Tünel baglantisi baslatiliyor... Lutfen bekleyin.
echo Bu islem biraz zaman alabilir.
cd /d "%~dp0"
call npx expo start --tunnel
pause
