
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

import requests

# just copy pasted from neptune lmao :skull:
def webhook_spammer():
    clear()
    showbanner()
    url = input(f"                        {w}[{cs[1]}~{w}] {cs[1]}Webhook URL: {w}").strip()
    content = input(f"                        {w}[{cs[1]}~{w}] {cs[1]}Message: {w}").strip()
    data = {'content': content}
    while True:
        try:
            response = requests.post(url, json=data, proxies=getrandomproxy())
            if response.status_code == 204:
                print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Sent {w}~> {cs[1]}{content}{re}")
            else:
                print(f"                        {w}[{red}!{w}] {red}{response.status_code}{re}")
        except requests.RequestException as e:
            print(f"                        {w}[{red}!{w}] {red}{e}{re}")

def delete_webhook():
    clear()
    showbanner()

    webhook_url = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Webhook URL: {w}")
    print()

    response = requests.delete(webhook_url, proxies=getrandomproxy())

    if response.status_code == 204:
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]} Webhook deleted successfully!{re}")
    else:
        print(f"                        {w}[{red}~{w}] {red} Failed to delete webhook {w}|{red} {response.status_code}{re}")

    input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]} Press enter {cs[2]}to continue.{re}")
    return

def get_webhook_info():
    clear()
    showbanner()

    webhook_url = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Webhook URL: {w}")
    print()
    response = requests.get(webhook_url, proxies=getrandomproxy(),)
    
    if response.status_code == 200:
        webhook_data = response.json()
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]} ID         {w}> {cs[1]}{webhook_data.get('id', 'Unknown')}{re}")
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]} Name       {w}> {cs[1]}{webhook_data.get('name', 'Unknown')}{re}")
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]} Channel ID {w}> {cs[1]}{webhook_data.get('channel_id', 'Unknown')}{re}")
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]} Guild ID   {w}> {cs[1]}{webhook_data.get('guild_id', 'Unknown')}{re}")
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]} Token      {w}> {cs[1]}{webhook_data.get('token', 'Unknown')}{re}")
    else:
        print(f"                        {w}[{red}!{w}] {red} Failed to fetch {w}~> {red}{response.status_code}{re}")

    input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]} Press enter {cs[2]}to continue.{re}") 
    return

def webhookmen():
    clear()
    showbanner()
    print(f"{cs[3]}                                                 Webhook Menu")
    print(f"\n                            {cs[0]}      <01>{cs[1]} {w}Webhook Spammer")
    print(f"                            {cs[0]}      <02>{cs[1]} {w}Webhook Info")
    print(f"                            {cs[0]}      <03>{cs[1]} {w}Webhook Delete")
    choice = input(f"\n                         {cs[0]}      NEP{cs[1]}TUN{cs[2]}E {w}» ")
    if choice == '1':
        webhook_spammer()
    elif choice == '2':
        get_webhook_info()
    elif choice == '3':
        delete_webhook()
    else:
        return
