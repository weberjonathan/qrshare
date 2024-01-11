:: Launch script for qrshare.py for use on PATH
:: Script version 1.0

:: Expected directory structure:
:: |- bin
::   |- qrshare.bat
:: |- qrshare
::   |- embed.jpg
::   |- qrshare.py

@echo off

:: find base directory
for %%i in ("%~dp0..") do set "basedir=%%~fi"

:: locate qrshare
set qrshare="%basedir%\qrshare\qrshare.py"

:: launch qr share
python %qrshare% %*