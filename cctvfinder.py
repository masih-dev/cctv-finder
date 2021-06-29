#!/bin/python3.8
# powered by masih ghorbani under GPL License
# warning : This project is designed for better Python learning. 
# Please do not use it inaccurate !!

from sys import exit
from time import sleep
from random import choice
from googlesearch import search
from pyfiglet import figlet_format as figlet


# Using this function we can search on Google and display the results to the user
def search_method(query):
    for j in search(query,tld="co.in", num=10, stop=10, pause=10):
        print (f"{colors.GREEN}-{colors.END}  {j}")
        sleep(2)

# on this class we have some colors code
class colors:
    END = '\033[0m'
    GREEN = '\033[92m'

print (figlet("CCTV finder",font="slant"))

with open("desc","r") as descfile:
    description = descfile.read()
    descfile.close()

print (description)

# In this array, we have several DORK to find vulnerable cameras.
dorks = [

    "inurl:”CgiStart?page=”",
    "inurl:/view.shtml",
    "intitle:”Live View / – AXIS",
    "inurl:view/view.shtml",
    "inurl:ViewerFrame?Mode=",
    "inurl:ViewerFrame?Mode=Refresh",
    "inurl:axis-cgi/jpg",
    "inurl:axis-cgi/mjpg (motion-JPEG) (disconnected)",
    "inurl:view/indexFrame.shtml",
    "inurl:view/index.shtml",
    "inurl:view/view.shtml",
    "liveapplet",
    "intitle:”live view” intitle:axis",
    "intitle:liveapplet",
    "allintitle:”Network Camera NetworkCamera” (disconnected)",
    "intitle:axis intitle:”video server”",
    "intitle:liveapplet inurl:LvAppl",
    "intitle:”EvoCam” inurl:”webcam.html”",
    "intitle:”Live NetSnap Cam-Server feed”",
    "intitle:”Live View / – AXIS”",
    "intitle:”Live View / – AXIS 206W”",
    "intitle:”Live View / – AXIS 210?",
    "inurl:indexFrame.shtml Axis",
    "inurl:”MultiCameraFrame?Mode=Motion” (disconnected)",
    "intitle:start inurl:cgistart * intitle:”WJ-NT104 Main Page”",
    "intitle:snc-z20 inurl:home/",
    "intitle:snc-cs3 inurl:home/",
    "intitle:snc-rz30 inurl:home/",
    "intitle:”sony network camera snc-p1?",
    "intitle:”sony network camera snc-m1?",
    "site:.viewnetcam.com -www.viewnetcam.com",
    "intitle:”Toshiba Network Camera” user login",
    "intitle:”netcam live image” (disconnected)",
    "intitle:”i-Catcher Console – Web Monitor”"
]

# Getting input from the user and selecting an option
option = int(input(f"""
{colors.GREEN}Please select one of the following.{colors.END}:

{colors.GREEN}[1]{colors.END} Search with random dork
{colors.GREEN}[2]{colors.END} Search with custom dork
{colors.GREEN}[3]{colors.END} Exit from CCTV finder

: """))

# In this case, a DORK is randomly selected and its search results are available
if option == 1:
    try:
        random_dork = choice(dorks)
        print (f"Search using this dork : {colors.GREEN}{random_dork}{colors.END}")
        search_method(query=random_dork)

    except:
        print (f"{colors.GREEN}\n*HTTP Error 429: Too Many Requests{colors.END}")
        print ("-Please try again at another time.")

# And in this case, the user can select a DORK and do the search.
elif option == 2:
    try:
        for i in range(0,34):
            print (f"{[i]} {dorks[i]}")
        numd = int(input("\n: "))
        if numd >= 0 and numd <=34:
            print (f"You selected : {colors.GREEN}{dorks[numd]}{colors.END}")
            search_method(query=dorks[numd])
        else:
            print (f"{colors.GREEN}Error : The number is out of range !{colors.END}")

    except:
        print (f"{colors.GREEN}\n*HTTP Error 429: Too Many Requests{colors.END}")
        print ("-Please try again at another time.")

elif option == 3:
    print (f"{colors.GREEN}Good,Bye!{colors.END}")
    exit()

else:
    print (f" {colors.GREEN}*Error{colors.END} : The number is out of range")
