from playground import Tic_Tac_Toe as TTT
from functions import show_playground
from functions import player_1, player_2, list_of_coordinates




print("\n\nWelcome to Tic Tac Toe match!\n")
size_x = int(input("Please set size of axis x (max. 25): "))
size_y = int(input("Please set size of axis x (max. 99): "))

playground = TTT(size_x, size_y)
field = playground.game_field()

print("\nPlease enter coordinates like 'A3'.\n"
    "Enter 'q' for exit the game.\n")
show_playground(field)


while True:

    player_1_coordinates = list_of_coordinates((input("\nPlayer one turn: \n")).upper())
    if player_1_coordinates == 'q' or player_1_coordinates == "Q":               # ???how to use only one IF to break main and secondary loop together???
        print("Good bye.")
        break
    player_1(field, player_1_coordinates)
        


    player_2_coordinates = list_of_coordinates((input("\nPlayer two turn: \n")).upper())
    if player_2_coordinates == 'q' or player_2_coordinates == "Q":              # can't use .lower() beacause I make variable as list
        print("Good bye.")
        break
    player_2(field, player_2_coordinates)


