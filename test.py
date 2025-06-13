import time
from colorama import Fore, init, Style

def print_with_colour(deck):
    joe = []
    for i in deck:
        if i[0] == "B":
            i = Fore.BLUE + Style.BRIGHT + i + Style.RESET_ALL
            joe.append(i)
        elif i[0] == "Y":
            i = Fore.YELLOW + Style.BRIGHT + i + Style.RESET_ALL
            joe.append(i)
        elif i[0] == "R":
            i = Fore.RED + Style.BRIGHT + i + Style.RESET_ALL
            joe.append(i)
        elif i[0] == "G":
            i = Fore.GREEN + Style.BRIGHT + i + Style.RESET_ALL
            joe.append(i)
    
    print(joe)
    return joe

deck = ["B1", "Y3", "G4", "R5"]
deck = print_with_colour(deck)

