
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

import threading

def replyspammer():    
    clear()
    showbanner()

    channel_id = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Channel ID: {w}")
    msg_id = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Message ID: {w}")
    msg = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Message: {w}")

    clear()
    showbanner()

    def reply_spammer(token, session, channel_id, message_id, msg):
        payload = {
            'content': msg,
            'tts': False,
            'message_reference': {
                "channel_id": channel_id,
                "message_id": message_id
            }
        }

        try:
            response = session.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                json=payload,
            )
            
            with threading.Lock():
                if response.status_code in [200, 201, 204]:
                    print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Success {w}~> {cs[1]}{token[:-35]}************{re}")
                elif response.status_code == 429:
                    print(f"                        {w}[{ye}~{w}]{ye} Ratelimit {w}~> {ye}{token[:-35]}************{re}")
                else:
                    print(f"                        {w}[{red}~{w}] {red}Failed {w}~> {red}{token[:-35]}************{re}")
        except Exception as e:
            with threading.Lock():
                print(f"                        {w}[{red}~{w}]{red} Error {w}~> {cs[2]}{token[:-35]}************{re}: {e}")
    
    with open('input/tokens.txt', 'r') as file:
        tokens = file.read().splitlines()

    while True:
        threads = []
        for token in tokens:
            session = getsession(token)
            for _ in range(20):
                t = threading.Thread(target=reply_spammer, args=(token, session, channel_id, msg_id, msg))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
