import time
import os
import sys
import random
from colorama import Fore, init


which = input(Fore.GREEN + "Do you want to use the what your number says about you? (1) or the Quote Generator(2)")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)


if which == "1":  
  n = input(Fore.GREEN + "What is your favorite number between one to nine: \n")
  f = open("num.txt", 'a')
  f.write(f"{n}\n")
  f.close()
  youare = "Your number says that you are"
  if n == "1":
    slowprint(f"{youare} a nice and intelligent person")
    
  if n == "2":
    slowprint(f"{youare} a nice and intelligent person.")
  if n == "3":
    slowprint(f"{youare} a nice and intelligent person.")
  if n == "4":
    slowprint(f"{youare} a nice and intelligent person.")
  if n == "5":
    slowprint(f"{youare} a nice and intelligent person.")
  if n == "6":
    slowprint(f"{youare} a nice and intelligent person.")

  if n == "7":
    slowprint(f"{youare} a nice and intelligent person.")
  if n == "8":
    slowprint(f"{youare} a nice and intelligent person.")
  if n == "9":
    slowprint(f"{youare} ")


if which == "2":
  fee = open("quotes.txt", 'r').read().splitlines()
  fe = random.choice(fee)
  print("Here's a quote for you!")
  slowprint(f"{fe}")