from colorama import Fore, Back, Style
import  random
import time
from time import sleep
import os 
deck = [ 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS', 
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS',
         'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'RS', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'YS',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'GS',
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'BS',
         'W+4', 'W+4']

random.shuffle(deck)
def print_slow(txt):
    for x in txt:                     
        print(x, end='', flush = True)  
        sleep(0.025)
    return None
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
        print_slow(deck1[i], end = " ")
def print_with_colour(txt):
    pass

def introduction():
    os.system('clear')
    print_slow("Welcome to two player UNO by Thierry")
    print()
    print_slow('Do you want to review the rules?(Y/N): ')
    rules = input()
    while rules != "N" and rules != "Y":
        print_slow("Please reenter with (Y/N)")
        rules = input()
    print()
    if rules != "N":
        print_slow("""You can play a card when it matches either the colour or number of the card, 
or if you have any wild cards. You must draw a card from the draw pile if you have no playable cards. 
The aim of UNO is to be the first player to eliminate all their cards so you'll want to avoid picking up 
cards as best you can.""")
        print()
        
    for i in range(101):
        print(Style.BRIGHT + Fore.CYAN + f"\rLoading: {i}%", end="")
        time.sleep(0.05)

    print(Style.RESET_ALL)
    print()
        
def distribute_cards(number, deck):
    player_deck = []
    for i in range(number):
        x = deck.pop(i)
        player_deck.append(x)

    return player_deck

def next_turn():
    sleep(2)
    os.system('clear')
    print_slow("The player's turn has ended. Please pass the laptop to the next user")
    print()
    print_slow("Has the laptop passed to the next user? (Y/N): ")
    ready = input()
    while ready.upper() != 'Y':
        print_slow("OK, now has the laptop been passed (Y/N): ")
        ready = input()
    os.system('clear')

def draw_card(player_deck, deck):
    random.shuffle(deck)
    x = deck.pop(0)
    player_deck.append(x)
    return player_deck

def play_card(player_deck,other_player_deck,center_card, deck, main_player, other_player):
    repeat = False
    print_slow("Centre card: {}".format(center_card))
    print()
    print_slow("{}, this is your deck: {}".format(main_player))
    print_with_colour(player_deck)
    print()
    print_slow("What card do you wish to place?, press 'd' to draw card: ")
    card = input()

    while card not in player_deck and card != 'd':
        print_slow("This card is not in your deck, please reenter")
        print()
        print_slow("What card do you wish to place?, press 'd' to draw card: ")
        card = input()

    if card == 'd':
        player_deck = draw_card(player_deck, deck)
        print_slow("You have drawn the card!")
        print()
        print()


    if card in player_deck:
        while card[0] != center_card[0] and card[1] != center_card[1] and card != "W+4":
            print_slow("This card is not valid, please reenter, press 'd' to draw card: ")
            card = input()
            if card == 'd':
                draw_card(player_deck, deck)
                break
        
        print()
        print_slow("{} is successfully placed".format(card))
        print()
        player_deck.remove(card)
        center_card = card

    if "S" in card:
        print()
        print_slow("Since {}'s turn is skipped, it is {}'s turn again!".format(other_player, main_player))
        repeat = True
    
    if "+2" in card:
        print()
        print_slow("Two cards are added to {}'s deck".format(other_player))
        for i in range(2):
            other_player_deck = draw_card(other_player_deck, deck)
    if "W" in card:
        print()
        print_slow("Since you got a wild card, choose a colour to proceed (R,B,Y,G): ")
        colour = input()
        while colour != "R" and colour != "B" and colour != "Y" and colour != "G":
            print_slow("Invalid, please reenter with (R,B,Y,G): ")
            colour = input()

        if colour == "R":
            center_card = "RED"
        elif colour == "B":
            center_card = "BLUE"
        elif colour == "Y":
            center_card = "YELLOW"
        elif colour == "G":
            center_card = "GREEN"

        print()
        print_slow("Four cards are added to {}'s deck".format(other_player))
        for i in range(4):
            other_player_deck = draw_card(other_player_deck, deck)

    while repeat == True:
        print()
        center_card, player_deck, other_player_deck, repeat = play_card(player_deck, other_player_deck, center_card, deck, main_player, other_player)

    return center_card, player_deck, other_player_deck, repeat

def check_deck(deck):
    if len(deck) <= 5:
        deck = [ 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'R⏭', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'Y⏭',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'G⏭', 
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'B⏭',
         'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'R⏭', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'Y⏭',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'G⏭',
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'B⏭',]
        random.shuffle(deck)
    return deck

def main(deck):
    introduction()
    center_card = deck.pop(0)
    while "W" in center_card:
        deck.append("W+4")
        center_card = deck.pop(0)

    player1_deck = distribute_cards(7,deck)
    player2_deck = distribute_cards(7,deck)

    print_slow("Player1, enter your name: ")
    player1 = input()
    print_slow("Player2, enter your name: ")
    player2 = input()
    print()
    print_slow("{} starts first!".format(player1.capitalize()))
    sleep(2)
    os.system('clear')

    while len(player1_deck) != 0 or len(player2_deck) != 0:
        center_card, player1_deck, player2_deck, repeat = play_card(player1_deck, player2_deck,center_card,deck, player1, player2)
        check_deck(deck)
        next_turn()
        center_card, player2_deck, player1_deck, repeat = play_card(player2_deck, player1_deck,center_card,deck, player2, player1)
        check_deck(deck)
        next_turn()
        
    os.system('clear')
        
    if len(player1_deck) == 0:
        print_slow("Congrats, {} has won!".format(player1))
    else:
        print_slow("Congrats, {} has won!".format(player2))
    
main(deck)


