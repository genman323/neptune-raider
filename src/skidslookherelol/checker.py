
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

def checker():
    clear()
    showbanner()
    twerking = []
    for token in tokens:
        response = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": f"{token}"}, proxies=getrandomproxy()).status_code
        if response in [201,200,204]:
            print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Working {w}~> {cs[1]}{token[:-35]}************{re}")
            twerking.append(token)
        elif response in [401,403]:
            print(f"                        {w}[{red}~{w}] {red}Failed {w}~> {red}{token[:-35]}************{re}")
        else:
            print(f"                        {w}[{red}!{w}] {red} Error {w}~> {red}{token[:-35]}************{re} {w}| {response}")
    
    choice = input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]}Save Tokens? (y/n): {w}")
    if choice.lower() in ["y", "yes", "ye", "ys", "es"]:
        with open("input/tokens.txt", "w") as file:
            file.write("\n".join(twerking))
    else:
        pass
    
    input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]}Press enter {cs[2]}to continue.")
    return
