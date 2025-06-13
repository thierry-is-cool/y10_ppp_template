import time
from colorama import Fore, init, Style

def print_with_colour(deck):
    deck1 = []
    for i in deck:
        if i[0] == "B":
            i = Fore.BLUE + Style.BRIGHT + i + Style.RESET_ALL
            deck1.append(i)
        elif i[0] == "Y":
            i = Fore.YELLOW + Style.BRIGHT + i + Style.RESET_ALL
            deck1.append(i)
        elif i[0] == "R":
            i = Fore.RED + Style.BRIGHT + i + Style.RESET_ALL
            deck1.append(i)
        elif i[0] == "G":
            i = Fore.GREEN + Style.BRIGHT + i + Style.RESET_ALL
            deck1.append(i)

    for i in range(len(deck1)):
        print(deck1[i], end = " ")

deck = ["B1", "Y3", "G4", "R5"]
deck = print_with_colour(deck)
