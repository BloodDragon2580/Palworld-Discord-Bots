**THIS IS ASSUMING YOU ALREADY HAVE YOUR BOT CREATED IN DISCORD DEVELOPER AND HAVE INVITED IT TO YOUR SERVER**

----

__OPTIONAL__

**Recommended NotePad++**
Open PowerShell
```
winget install -e --id Notepad++.Notepad++
```

Close PowerShell

__OPTIONAL__

----

Open PowerShell
```
winget install -e --id Python.Python.3.12
```

Enter 'Y' and hit Enter

```
winget install --id Git.Git
```

Restart computer/host

----

Open PowerShell

```
cd "pathyouwantbot"
```

Example For Desktop (We will make the palworld-bot folder separately)
```
cd C:\Users\"YOURUSERNAME"\Desktop
```

```
git clone https://github.com/dkoz/palworld-bot
```
```
cd palword-bot
```
```
Set-ExecutionPolicy RemoteSigned
```
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
```
```
pip install setuptools
```
```
cp .env.example .env
```
```
cp data/config.json.example data/config.json
```

Minimize PowerShell

----

Open 'palworld-bot' Folder
Right click '.env' and select 'Edit in NotePad++'
Configure the environment variables and save.

Open 'data' folder
Right click 'config.json' and select 'Edit in NotePad++'
Configure the server information.

Close File Explorer

----

Restore PowerShell Window

```
python .\main.py
```

----

Configure Bot on Discord

__**TROUBLESHOOTING**__

__Error:__
```
winget : The term 'winget' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pipe
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (winget:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```
__Solution:__
Install winget and restart.
https://github.com/microsoft/winget-cli/releases/download/v1.6.3482/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
