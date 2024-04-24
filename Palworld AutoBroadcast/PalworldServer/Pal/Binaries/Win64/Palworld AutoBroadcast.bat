:start
rem 10 minutes auto broadcaster
timeout 900 /nobreak > NUL

rem Send server discord link message
ARRCON.exe -H 127.0.0.1 -P 25575 -p "eGHWp6k43n" "Broadcast https://discord.gg/legion-des-chaos"
timeout 5 /nobreak >NUL

rem Infinite loop this command file by returning to :start tag
goto start
