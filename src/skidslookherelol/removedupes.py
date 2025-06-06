
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

import string

def removedupes():
    clear()
    showbanner()

    tokens_file = "input/tokens.txt" # skid this dookie dupes remover, just change the file man 😎 
    
    with open(tokens_file, "r") as file:
        tokens = [line.strip() for line in file.readlines() if line.strip()]

    unique_tokens = list(set(tokens))
    duplicates_removed = len(tokens) - len(unique_tokens)
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    backup_file = f"input/backup-{random_string}-tokens.txt"

    with open(backup_file, "w") as file:
        file.write("\n".join(tokens))
    
    with open(tokens_file, "w") as file:
        file.write("\n".join(unique_tokens))

    if duplicates_removed > 0:
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Removed duplicates{cs[2]}: {duplicates_removed} removed")
    else:
        print(f"                        {w}[{cs[1]}~{w}] {cs[1]}No duplicates found")

    print(f"                        {w}[{cs[1]}~{w}] {cs[1]}Backup created {w}- {cs[2]} {backup_file}")
    input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]}Press enter{cs[2]} to continue.")
    return
