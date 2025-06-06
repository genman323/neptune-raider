
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

import os
import random
import time
import json
import webbrowser
import ctypes
import tls_client
from valdemarcord import Discord #------ using this for headers till i got my own api up

tokens = open("input/tokens.txt").read().splitlines()
proxies = open("input/proxies.txt").read().splitlines()


# if u want you can add more
emojilist = [
    '😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😇', '😈', '😉', '😊', '😋', '😌',
    '😍', '🥰', '😘', '😗', '😙', '😚', '😜', '😝', '😛', '🤑', '😏', '😒', 
    '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩',
    '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥',
    '😓', '🤗', '🙄', '😶', '😐', '😑', '😬', '🤨', '🤢', '🤮', '🤧', '😷', '🥴', '😴',
    '😶‍🌫️', '🤠', '🥳', '💩', '🔥', '🧊', '😈', '👿', '👹', '👺', '💀', '☠️', '😾', '🙀',
    '👎', '🖕', '💔', '🔪', '🪓', '⛓️', '⚰️', '🪦', '🩸', '😡', '🤬', '🥀', '🗑️', '⚠️',
    '🔞', '🔇', '🚫', '❌', '🛑', '😤', '😠', '😒', '🙄', '😑', '🤥', '👎', '👊', '🖕',
    '🤡', '🐍', '🦀', '🦶', '🚷', '💣', '💥', '😵‍💫', '🌍', '🛠️', '🪛', '🗡️', '🔨'
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
showbanner()
print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Building Headers...")

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,pl;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://discord.com',
    'Priority': 'u=1, i',
    'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': Discord._fetch_useragent(),
    'X-Debug-Options': 'bugReporterEnabled',
    'X-Discord-Locale': 'en-US',
    'X-Discord-Timezone': 'Europe/Berlin',
    'X-Super-Properties': Discord.get_x_super_properties()
}


    
def getrandomproxy():
    prox = random.choice(proxies)
    prox4 = {
        "http": f"https:{prox}"
    }
    return prox4

def settitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def chromevers() -> str:
    try:
        response = requests.get("https://versionhistory.googleapis.com/v1/chrome/platforms/linux/channels/stable/versions")
        data = json.loads(response.text)
        return data['versions'][0]['version']
    except Exception:
        return None

def getsession(token: str = "", cookie: bool = True):
    ident = {
        "Windows": f"chrome_{chromevers()[:3]}"
    }["Windows"]  

    session = tls_client.Session(
        client_identifier=ident,
        random_tls_extension_order=True
    )
    
    session.headers = headers
    if token:
        session.headers.update({"Authorization": token})
    if cookie:
        site = session.get("https://discord.com")
        session.cookies = site.cookies

    return session
