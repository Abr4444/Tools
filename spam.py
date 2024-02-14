import pyautogui
import asyncio
import colorama
import os
import time
import signal
import fade
import sys
import ctypes
from colorama import Fore, Back, Style, init
from colorama import just_fix_windows_console

just_fix_windows_console()
ctypes.windll.kernel32.SetConsoleTitleW("Spammer | by Abr")
os.system('color FF')
os.system("cls")


banner="""

    ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
  ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
  ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
    ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
  ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
        ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                  
"""
check=True
while check==True:
  faded_banner = fade.pinkred(banner)
  print(faded_banner)

  confirm=input(" [·] Do you want to use the spammer(y,n):  ")  
  if confirm=="y":
    os.system("cls")                   
    print(faded_banner)
    amount=int(input(" [·] How many times do you want to spam:  "))
    text=str(input(" [·] What message do you want to spam: "))
    sleep=float(input(" [·] What cooldown do you want between messages: "))
    os.system("cls") 
    print(faded_banner)
    print("    [·] Spamming in 3\n           ")
    time.sleep(1)
    print("    [·] Spamming in 2\n           ")
    time.sleep(1)
    print("    [·] Spamming in 1          ")
    time.sleep(1)

    for i in range(amount):
        pyautogui.write(text+"\n")
        pyautogui.press("enter")
        time.sleep(sleep)
        os.system("cls")
        
  else:
    text= input(" \n [·] Do you want to close the program?(y,n):  ")
    if text=="n":
      os.system("cls")
    else:
      os.system("cls")
      quit()

    























