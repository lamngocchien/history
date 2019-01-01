@echo off
mode 800
call py-dist\scripts\env.bat
cd py-dist\
python run.py
pause