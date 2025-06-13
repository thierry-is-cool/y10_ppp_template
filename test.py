import time
from colorama import Fore, init, Style

init()

for i in range(101):
    print(Style.BRIGHT + Fore.CYAN + f"\rProgress: {i}%", end="")
    time.sleep(0.1)