import os
import time
import requests
from datetime import datetime, timedelta

WEBHOOK_URL = 'https://discord.com/api/webhooks/1232440200958050345/okf3aXAIab6kmf_JXHLQEnwGTnm0fqNzkGSvJLwtTWy2XkUP7-bH49wp1mrtgAAfxO3Y' # Put here you Discord webhook

# Path to the text log files
CHATLOG = 'C:/WindowsGSM/servers/3/serverfiles/Pal/Binaries/Win64/PalChatLog.txt'

LOG_FILES = [CHATLOG]

f= open ('PalChatLogLogo.txt','r')

print(''.join([line for line in f]))

def discord_logs(content):
    data = {
        "content": content
    }
    requests.post(WEBHOOK_URL, json=data)


def main():
    log_file_last_lines = {}
    for log_file in LOG_FILES:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                lines = f.readlines()
                if lines:
                    log_file_last_lines[log_file] = lines[-1]
                else:
                    log_file_last_lines[log_file] = ''
        else:
            log_file_last_lines[log_file] = ''

    while True:
        for log_file in LOG_FILES:
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    if lines and lines[-1] != log_file_last_lines[log_file]:
                        current_time = datetime.now().strftime('%m-%d %H:%M:%S')
                        new_content = ''.join(lines[len(lines) - len(log_file_last_lines[log_file].split('\n')):])
                        log_type = os.path.basename(log_file).split('.')[0].upper()
                        if 'error' in log_file.lower():
                            discord_logs(f'❗️ **{log_type}** Palworld Chat Datum, Uhrzeit: {current_time} **ERROR LOG:** ```diff\n-{new_content}```') # For ERRORS
                        else:
                            discord_logs(f'📃 **{log_type}** Palworld Chat Datum, Uhrzeit: {current_time} **LOG:** ```css\n{new_content}```') # For LOGS
                        log_file_last_lines[log_file] = lines[-1]
        time.sleep(1)

if __name__ == '__main__': # Everything in loop in case of any error
    while True:
        try:
            main()
        except Exception as error:
            error_message = f'❗️ An error occurred ERROR: \n{str(error)}'
            print(f'An error occurred ERROR: \n{str(error)}')
            discord_logs(error_message)
            continue
