import  random
import os 
deck = [ 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'R⏭', 'R↻', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'Y⏭', 'Y↻',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'G⏭', 'G↻',
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'B⏭', 'B↻',
         'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6','R7', 'R8', 'R9', 'R+2', 'R⏭', 'R↻', 
         'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6','Y7', 'Y8', 'Y9', 'Y+2', 'Y⏭', 'Y↻',
         'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6','G7', 'G8', 'G9', 'G+2', 'G⏭', 'G↻',
         'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7', 'B8', 'B9', 'B+2', 'B⏭', 'B↻']
random.shuffle(deck)

def introduction():
    os.system('clear')
    rules = input('Do you want to review the rules?(Y/N)')
    while rules != "N" and rules != "Y":
        rules = input("Please reenter with (Y/N)")
    print()
    if rules != "N":
        print("""You can play a card when it matches either the colour or number of the card, 
or if you have any wild cards. You must draw a card from the draw pile if you have no playable cards. 
The aim of UNO is to be the first player to eliminate all their cards so you'll want to avoid picking up 
cards as best you can.""")
        print()
        
def distribute_cards(number, deck):
    player_deck = []
    for i in range(number):
        x = deck.pop(i)
        player_deck.append(x)

    return player_deck

def next_turn():
    ready = input("Has the laptop passed to the next user? (Y?N)")
    while ready.upper() != 'Y':
        ready = input("OK, now has the laptop been passed (Y/N)")
    if ready  == 'Y':
        os.system('clear')

def draw_card(player_deck, deck):
    x = deck[0]
    player_deck.append(x)
    return player_deck

def play_card(player_deck,other_play_deck,center_card, deck, main_player, other_player):
    print("{}, this is your deck: {}".format(main_player, player_deck))
    print()
    card = input("What card do you wish to place?, press 'd' to draw card")

    while card not in player_deck and card != 'd':
        print("This card is not in your deck, please reenter")
        card = input("What card do you wish to place?, press 'd' to draw card")

    if card == 'd':
        draw_card(player_deck, deck)

    if card in player_deck:
        while card[0] != center_card[0] and card[1] != center_card[1]:
            card = input("This card is not valid, please reenter, press 'd' to draw card")
            if card == 'd':
                draw_card(player_deck, deck)
                break

        player_deck.remove(card)
        center_card = card
      
def main(deck):
    introduction()
    center_card = deck[0]
    player1_deck = distribute_cards(7,deck)
    player2_deck = distribute_cards(7,deck)

    player1 = input("Player1, enter your name: ")
    player2 = input("Player2, enter your name: ")
    print()
    print("{} starts first!".format(player1.capitalize()))
    os.system('clear')

    while len(player1_deck) != 0 or len(player2_deck) != 0:
        play_card(player1_deck, player2_deck,center_card,deck, player1, player2)


    
main(deck)

