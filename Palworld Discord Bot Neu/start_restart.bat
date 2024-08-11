@echo off
echo Starte main.py...

:loop
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo main.py ist abgestürzt oder wurde beendet. Neustart...
    timeout /t 5
    goto loop
)

echo main.py wurde beendet.
pause
