import sys
try:
    print('')
except SyntaxError as e:
    if e == True:
        print("Hey Idiot, Use python3.")   
import time
print("Please Wait.. The Tools Is Loading Assets..")
time.sleep(2)
try:
    print("Checking For Module..")
except ModuleNotFoundError as e:
    if e == True:
        print('Module Not Found: ', (e))
        
import time
import os
from os.path import exists
import googlesearch
import wget
import urllib.request
import colorama
from colorama import Fore, Style, init
import random
import socket
import requests
import sys
from googlesearch import search
from subprocess import getoutput
import argparse
import ipaddress
import faker
from faker import Faker
from bs4 import BeautifulSoup
import re
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from pythonping import ping
import exiftool
import openai
import importlib

global user_ip
user_ip = Faker()
ip_addr = user_ip.ipv4()
ip_address = user_ip.ipv6()
MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1


def random_ipv4():
    return  ipaddress.IPv4Address._string_from_ip_int(
        random.randint(0, MAX_IPV4)
    )

def random_ipv6():
    return ipaddress.IPv6Address._string_from_ip_int(
        random.randint(0, MAX_IPV6)
    )
random.seed(444)
random_ipv4()
'79.19.184.109'
random_ipv4()
'3.99.136.189'
random_ipv4()
'124.4.25.53'
random_ipv6()
'4fb7:270d:8ba9:c1ed:7124:317:e6be:81f2'
random_ipv6()
'fe02:b348:9465:dc65:6998:6627:1300:29c9'
random_ipv6()
'74a:dd88:1ff2:bfe3:1f3:81ad:debd:db88'    
address = random_ipv4()
ip6 = random_ipv6()

global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT
    
if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
    os.system('clear')
elif os.name == 'nt':   # Untuk sistem Windows
    os.system('cls')
red = '\033[1;91m'
white = '\033[37m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'


package_name = "adafruit"

try:
    pass
except ImportError or ModuleNotFoundError:
    importlib.import_module(package_name)
    print(info + f"[ + ] Downloading adafruits ! [ + ]")
    os.system('pip3 install adafruit-io')
    os.system('pip install adafruit-circuitpython-adafruitio')
    os.system('pip install adafruit-circuitpython-motor')
    os.system('pip install adafruit-circuitpython-circuitplayground')

print(f"""
{red}
⠀⠀⠀⡠⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀
⠀⠀⣰⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⠀⠀⠀
⠀⢠⡇⠀⢸⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠈⠀⠀⡇⠀⠀
⠀⢸⡄⠀⠀⠢⣠⣴⡋⠉⠁⠀⠀⠀⠀⠀⠈⠻⣶⣄⡠⠃⠀⠀⡇⠀⠀
⡀⠈⣧⠀⠀⠀⠈⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⢠⠇⠀⡀
⣷⡀⠘⣆⠀⠀⠀⣿⠀⠀⠀⠀⠀⢀⣀⣠⡤⢾⣿⡁⠀⠀⢠⡟⠀⣴⡇
⡏⢻⣦⡘⣷⣦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠻⢷⣤⣴⡏⣠⡾⠃⠃
⢳⠀⠙⢿⣿⡏⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠣⡀⠀⠀⠀⢹⣿⠟⠀⢰⠀
⠈⢧⡀⢸⣿⣿⣀⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣀⠀⠈⣿⠀⢀⠌⠀
⠀⠀⠙⢾⣿⣿⣿⣿⡗⢄⡀⠀⡀⠀⡀⠀⡀⠔⡿⠀⠀⠀⣿⠔⠁⠀⠀
⠀⠀⠀⠀⢿⣿⡋⠉⠙⠒⠉⠙⡇⢀⡟⠉⠑⠊⠁⠀⠀⢠⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⡇⠀⠀⠀⢀⠀⠃⢸⣷⣀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣶⣶⣖⠛⠦⠀⠈⡿⠟⢑⣶⣶⣾⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣯⠉⢩⠧⠄⠓⠒⠁⣔⢵⠈⣡⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣧⠘⢜⣉⣁⣈⣉⣏⠄⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠐⠒⠒⠒⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⣀⣀⣀⣠⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⠉⠀⠀⠀
time.sleep(0.5)
print(info + f'            [ ]Remember !, If The Tools Had A Error, Please Waiting For The Update.[ ]')
print(f"""{yellow}┌─────────────────────────────────────────────────────────────────────────────────────────────────┐{blue}
[01] Dump V2 {red}
[02] Dump V1 {green}
{yellow}└─────────────────────────────────────────────────────────────────────────────────────────────────┘{blue}
""")⠀⠀⠀⠀⠀⠀⠀⠀
print('')
print(f'\033[37m')
print(f"╭─[{red} JawaBaratErorNetwork@root {white} ~/home")
answer = input("╰─$ ")
print('\033[1;32m\n')
if answer == ("1"):
    pass
    global domain

    global file_types
    file_types = ['doc', docx', dotx', 'dotm','ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'sql', 'txt']
                   
    print ("""
    ██████▀▀▀░░░░▀▀▀██████
    ███▀░░░░░░░░░░░░░░▀███
    ██│░░░░░░░░░░░░░░░░│██
    █▌│░░░░░░░░░░░░░░░░│▐█
    █░└┐░░░░░░░░░░░░░░░┌┘█
    █░░└┐░░░░░░░░░░░░░┌┘░█
    █░░┌┘▄▄▄▄░░░░▄▄▄▄▄└┐░█
    █▌░│████▌░░░▐█████│░▐█
    ██░│▐█▀▀░░▄░░▀▀██▌│░██
    █▀─┘░░░░░▐█▌░░░░░░└─▀█
    █▄░░▄▄▓░░▀█▀░░▓▄▄▄░░▄█
    █▄─┘██▌░░░░░░░░▐██└─▄█
    ██░░▐█─┬┬┬┬┬┬┬┬─█▌░░██
    █▌░░░▀. |┼.|┼|┼|┼▀ ░▐█
    ██▄░░░└┴┴┴┴┴┴┴┴┘░░▄█ █
    ████▄░░░░░░░░░░░░▄████
    ███████▄▄▄▄▄▄▄████████
    """)

    print("Dump Mode")
    print("Do Not Use Https")

    print(info + f"-" * 73)
    print("Internet Connection Required : 5MBps (To Optimal The Tools)")
    print(f'\033[1;32mDump Mode')
    target = input("\nTarget Site : ")
    dirt = ("")
    counter = 1
    counter = counter + 1

    os.makedirs(target)

    def download_files(*args):
        # Nama direktori tempat Anda ingin menyimpan file
        target_directory = target
        # Loop melalui argumen (hasil pencarian)
        for result in args:
            # Ekstrak nama file dari URL menggunakan urlparse
            parsed_url = urlparse(results)
            file_name = os.path.basename(parsed_url.path)

            # Gabungkan direktori dengan nama file
            file_path = os.path.join(target_directory, file_name)

            # Unduh file
            response = requests.get(results)

            # Simpan file ke direktori yang ditentukan
            if response == True:
                with open(file_path, "wb") as file:
                    file.write(response.content)

    def dorker():
        request = 0
        path = target
        isdir = os.path.isdir(path)
        if isdir == True:
            pass
        else:
            os.mkdir(target)  
        os.chdir(target)    
    for files in file_types:
       try: 
            file_exists = exists('.google-cookie')
            if file_exists == True:
             os.remove('.google-cookie')
            rand_user = random.choice(user_agents)
            rand_ipv4 = random.choice(address)
            rand_ipv6 = random.choice(ip6)
            print(info + f'\033[1;33m<!> Processing <!>: Searching Info For {files}..')
            for results in search(f'site:{target} filetype:{files}', tld='com', lang='en', num=3, start=0, stop=None, pause=10):
             print(success + f'[+]Found[+] : ')
             print(success + f'\033[1;33m{results}')
             wget.download(results, out=target)
             requ =+ 1
       except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
                 continue
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
                 continue
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
             else:
                 continue    
       except FileExistsError:
           print(fail + f'File {target} Exists.')
       except OSError:
                 continue
       except urllib.error.URLError:
                print(fail + f'[Error] File {files} could not be downloaded. Skipping.')
                continue
       except ModuleNotFoundError:
                print(fail + f'[Error] Did you already install requirements.txt?')
       except UnicodeDecodeError:
                continue 

    print ("Done...")
    print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
    print ("\t\t\033[1;91mExit\n\n")   
    exit()
    
    elif answer == ("2"):
    time.sleep(0.5)
    print("""\033[1;91m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀
⠀⠀⣰⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⠀⠀⠀
⠀⢠⡇⠀⢸⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠈⠀⠀⡇⠀⠀
⠀⢸⡄⠀⠀⠢⣠⣴⡋⠉⠁⠀⠀⠀⠀⠀⠈⠻⣶⣄⡠⠃⠀⠀⡇⠀⠀
⡀⠈⣧⠀⠀⠀⠈⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⢠⠇⠀⡀
⣷⡀⠘⣆⠀⠀⠀⣿⠀⠀⠀⠀⠀⢀⣀⣠⡤⢾⣿⡁⠀⠀⢠⡟⠀⣴⡇
⡏⢻⣦⡘⣷⣦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠻⢷⣤⣴⡏⣠⡾⠃⠃
⢳⠀⠙⢿⣿⡏⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠣⡀⠀⠀⠀⢹⣿⠟⠀⢰⠀
⠈⢧⡀⢸⣿⣿⣀⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣀⠀⠈⣿⠀⢀⠌⠀
⠀⠀⠙⢾⣿⣿⣿⣿⡗⢄⡀⠀⡀⠀⡀⠀⡀⠔⡿⠀⠀⠀⣿⠔⠁⠀⠀
⠀⠀⠀⠀⢿⣿⡋⠉⠙⠒⠉⠙⡇⢀⡟⠉⠑⠊⠁⠀⠀⢠⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⡇⠀⠀⠀⢀⠀⠃⢸⣷⣀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣶⣶⣖⠛⠦⠀⠈⡿⠟⢑⣶⣶⣾⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣯⠉⢩⠧⠄⠓⠒⠁⣔⢵⠈⣡⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣧⠘⢜⣉⣁⣈⣉⣏⠄⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠐⠒⠒⠒⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⣀⣀⣀⣠⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      LEAKER TOOLS BY ./ITINGSS 
""")
a1 = input(f"Target Site : ")
s = input(f"File Extension <example : pdf csv xls db> : ")
a = s.split()
filetypes = a
try:
    os.makedirs(a1)
    global file_types
    file_types = filetypes
    def dorker():
            request = 0
            path = a1
            isdir = os.path.isdir(path)
            if isdir == True:
                pass
            else:
                os.mkdir(a1)  
            os.chdir(a1)    
    counter = 1
    counter = counter + 1
    for files in file_types:
           try: 
                 req = 1
                 req = req + 1
                 file_exists = exists('.google-cookie')
                 if file_exists == True:
                  os.remove('.google-cookie')
                 rand_user = random.choice(user_agents)
                 rand_ipv4 = random.choice(address)
                 rand_ipv6 = random.choice(ip6)
                 print(info + f'\033[1;33m<!> Processing <!>: Searching Info For {files}..')
                 for results in search(f'site:{a1} filetype:{files}', tld='com', lang='en', num=int(req), start=0, stop=None, pause=10):
                     print(success + f'[+]Found[+] : ')
                     print(success + f'\033[1;33m{results}')
                     wget.download(results, out=a1)
                     requ =+ 1
           except urllib.error.HTTPError as e:
                 if e.code == 404:
                     print(fail + f' [404] Download Fail, Skipping')
                     continue
                 if e.code == 403:
                     print(fail + f' [403] Download Fail, Skipping')
                     continue
                 if e.code == 429:
                     print(fail + f' [429] Download Fail, Please Wait.')
                     time.sleep(5)
                 else:
                     continue    
           except OSError:
               continue
           except urllib.error.URLError:
               print(fail + f'[Error] File {files} could not be downloaded. Skipping.')
               continue
           except ModuleNotFoundError:
               print(fail + f'[Error] Did you already write python3 setup.py?')
           except UnicodeDecodeError:
               continue 
           except ValueError:
               continue

except OSError:
    print(f"File Failed Deleted, Please Delete Manually")
except FileExistsError:
    print(fail + f'File {a1} Exists.')
    os.removedirs(a1)
    print(success + f'Deleted')
except TypeError:
    print("Usage : python3 maung.py")
except ModuleNotFoundError:
    print(fail + f'[Error] Did you already write python3 setup.py?')
print ("Done...")
print ("\n\t\t\t\t\033[34mJawaBaratErorNetwork\033[0m")
print ("\t\t\033[1;91mExit\n\n")   
exit()
