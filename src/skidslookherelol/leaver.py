
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

import threading


def leaver():
    clear()
    showbanner()

    serverid = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Server ID: {w}")

    def leave_server(token):
        try:
            response = requests.delete(
                f"https://discord.com/api/v9/users/@me/guilds/{serverid}",
                headers={"Authorization": token},
                proxies=getrandomproxy(),
                data={"lurking": False},
                timeout=10
            )
            if response.status_code in [204, 200]:
                print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Left {w}~> {cs[1]}{token[:-35]}************{re}")
            elif response.status_code == 429:
                print(f"                        {w}[{ye}~{w}] {ye}Ratelimit {w}~> {ye}{token[:-35]}************{re}")
            else:
                print(f"                        {w}[{red}!{w}] {red}{response.status_code} {w}~> {red}{token[:-35]}************{re}")
        except requests.exceptions.Timeout:
            print(f"                        {w}[{red}!{w}] {red} Timeout {w}~> {red}{token[:-35]}************{re}")
        except Exception as e:
            print(f"                        {w}[{red}!{w}] {red} Error {e} {w}~> {red}{token[:-35]}************{re}")

    threads = []
    for token in tokens:
        threads.append(threading.Thread(target=leave_server, args=(token,)))

    for i in range(0, len(threads), 15):
        batch = threads[i:i + 15]
        for thread in batch:
            thread.start()
        for thread in batch:
            thread.join()

    input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]} Press enter {cs[2]}to continue.")
    return()
