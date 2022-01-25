
import requests
from colorama import Fore
import random
import threading

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text




def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


rs = requests.Session()

print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} You can encode it here: https://www.base64-image.de/')
img = input('Base64 img code: ')


def pfpchanger(token):
    try:
        headers = mainHeader(token)
        rd = rs.patch('https://discord.com/api/v9/users/@me', headers=headers,
                        json={'avatar': f'{img}'})
        if rd.status_code == 200:
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done!')
        else:
            print(
                f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error...")

    except:
        print('Error...')


tokens = open('tokens.txt', 'r').read().splitlines()
for token in tokens:
    threading.Thread(target=pfpchanger(token)).start()