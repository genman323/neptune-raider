
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *



import concurrent.futures
import string

class JoinerData:

    pass

class Instance(JoinerData):

    def __init__(self, client, token, invite, headers):
        self.client = client
        self.token = token
        self.invite = invite
        self.headers = headers

class Joiner: 



    def __init__(self, data: Instance) -> None:

        self.session = data.client
        self.session.headers = data.headers
        self.get_cookies()
        self.instance = data

    def rand_str(self, length: int) -> str:

        return "".join(random.sample(string.ascii_letters + string.digits, length))

    def get_cookies(self) -> None:

        site = self.session.get("https://discord.com")
        self.session.cookies = site.cookies
    

    def join(self) -> None:

        self.session.headers.update({"Authorization": self.instance.token})
        result = self.session.post(
            f"https://discord.com/api/v9/invites/{self.instance.invite}",
            json={
                "session_id": self.rand_str(32),
            },
        )
        if result.status_code == 200:
            print(f"                        {w}[{cs[1]}~{w}]{cs[1]} Joined {w}~> {cs[2]}{self.instance.token[:-35]}************{re}")
        else:
            json_result = result.json()
            if "captcha_key" in json_result:
                print(f"                        {w}[{ye}~{w}]{ye} Captcha {w}~> {ye}{self.instance.token[:-35]}************{re}")
            else:
                print(f"                        {w}[{red}~{w}]{red} Failed {w}~> {red}{self.instance.token[:-35]}************{re}")

class initialize:

    def start(i):
        Joiner(i).join()

def joiner():

    clear()
    showbanner()

    with open('input/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in file]
    
    instances = []
    invite = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Invite: {w}")
    invite = invite.replace("https://discord.gg", "").replace("discord.gg/", "")

    clear()
    showbanner()



    for i in range(len(tokens)):
        header = headers
        instances.append(Instance(
            client=tls_client.Session(
                client_identifier=f"chrome_{random.randint(110,115)}",
                random_tls_extension_order=True
            ),
            token=tokens[i],
            headers=header,
            invite=invite
        ))


    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(initialize.start, i) for i in instances]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"                        {w}[{red}~{w}]{red} Error {w}~> {red}{e}")

    input(f"\n                        {w}[{cs[1]}~{w}] {cs[1]}Press enter {cs[2]}to continue.")
    return
