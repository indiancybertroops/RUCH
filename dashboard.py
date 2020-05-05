import time
import os
import concurrent.futures
try:
	import requests
except ImportError:
	os.system("clear")
	os.system("pip install requests")
try:
	from colorama import *
except ImportError:
	os.system("clear")
	os.system("pip install colorama")
import time
os.system("clear")
auth = """ 
 ____   _    _  _____ _   _
|  _ \ | | | | / ____| | | |
| |_) || | | ||  |   | |_| |
|  _ < | |_| ||  |___|  _  |
|_| \_\ \\____/ \_____|_| |_|
        
    RUCH framework Admin Login bypass Finder 
    Team:IndianCyberTroops
    Developer:H4MM3R.PY
    VERSION:2.0
                        """
             
print(Style.BRIGHT)
print(Fore.GREEN+auth)
site = input(Fore.GREEN+" [-] LINK OF ADMIN PANEL: "+Fore.GREEN)
str = site.split("/")
site = site.replace(str[-1],"")
print()
try:
	opn = open("path.txt","r").readlines()
except:
	print(Fore.RED+"\n [+] Target List Not Found [+]")
	quit()
def scan(x):
	try:
		st = x.strip()
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		r = requests.get(site+st,timeout=10,headers=headers)
		code = int(r.status_code)
		if code < 400:
			print(Fore.BLUE+" Found --> "+site+st)
		else:
			print(Fore.GREEN+" Not Found -->"+site+st)
	except Exception as e:
		print(Fore.CYAN+" Refused Connection -->"+site)
try:
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(scan,opn)
except:
	print(Fore.GREEN+" [!] Connection Lost!")
print("\n"+Fore.BLUE+" [+] Scanned Finished [+] ")
print(Fore.RESET)