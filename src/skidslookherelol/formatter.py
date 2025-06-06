
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

def formatter(): 
    clear()
    showbanner()
    with open("input/tokens.txt", "w", encoding='utf-8') as output_file: 
        for token in tokens:
            if ":" in token:
                token_parts = token.strip().split(":")[2:]  
                new_token = ":".join(token_parts) + "\n"  
                output_file.write(new_token)
                print(f"                        {w}[{cs[1]}~{w}]{cs[1]} Success {w}~> {cs[2]}{token[:-35]}************{re}")
            else:
                print(f"                        {w}[{red}~{w}]{red} Failed {w}~> {red}{token[:-35]}************{re}")
                output_file.write(token + "\n")

        input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]} Press enter {cs[2]}to continue.")
        return()
