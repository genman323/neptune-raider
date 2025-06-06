
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *
from src.skidslookherelol import *
from src.skidslookherelol.formatter import *
from src.skidslookherelol.checker import *
from src.skidslookherelol.joiner import *
from src.skidslookherelol.leaver import *
from src.skidslookherelol.msgspam import *
from src.skidslookherelol.removedupes import *
from src.skidslookherelol.webhookmenu import *
from src.skidslookherelol.replyspam import *
import sys

clear()
settitle("Serenity [Private] - https://discord.gg/ArfGgxae")

def handler(option):
    actions = {
        "1": joiner, #joiner
        "2": leaver, #leaver
        "3": checker, #checker
        "4": formatter, #formatter 
        "5": premium,
        "6": premium,
        "7": premium,
        "8": premium,
        "9": removedupes, #rem dupes
        "10": premium,
        "11": messagespammer, #channel spam
        "12": premium,
        "13": premium,
        "14": replyspammer, #reply spam
        "15": premium,
        "16": premium,
        "17": premium,
        "18": webhookmen, #webhook menu
        "19": premium, 
        "20": premium,
        "D": discord, #discord
        "S": premium,
    } # poorons, go purchase

    action = actions.get(option)
    if action:
        action()
    else:
        return

while True:
    clear()
    choice = input(gui)

    if choice == "0":
        sys.exit
    
    handler(option=choice)
