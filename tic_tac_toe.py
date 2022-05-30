from functions import player_turn, show_playground, list_of_coordinates
from logging import raiseExceptions
from playground import Tic_Tac_Toe as TTT
from winner import Winner


# set playground parameters
print("\n\nWelcome to Tic Tac Toe match!\n")#
parameters_done = False
while parameters_done == False:
    try:
        size_x = int(input("Please set size of axis x (3-26): "))
        if size_x not in range(3, 27):
            raise TypeError("Number is not in given range!")

        size_y = int(input("Please set size of axis y (3-99): "))
        if size_y not in range(3, 100):
            raise TypeError("Number is not in given range!")

        symbol_in_row_to_win = int(input("Please set how many symbols in row to win (3-5): "))
        if symbol_in_row_to_win not in range(3, 6):
            raise TypeError("Number is not in given range!")
            
        parameters_done = True
    except:
        print("Please enter parameters in given range!")
        parameters_done = False
    

# make a playground
playground = TTT(size_x, size_y)                    # make an instance of Tic_Tac_Toe class
field = playground.game_field()

# make a list of draw check for each line check- can't make it in loop
check_draw_player_one = []      
check_draw_player_two = []


print("\nPlease enter coordinates like 'A3'.\n"
    "Enter 'q' for exit the game.\n")
show_playground(field)

game_turn = 1
while True:

    if game_turn % 2 != 0:              # every odd round is player one round
        player_symbol = "X"
        player = 'one'
        player_coordinates = (input(f"\nPlayer {player} turn: \n")).upper()
    else:
        player_symbol = "O"
        player = 'two'
        player_coordinates = (input(f"\nPlayer {player} turn: \n")).upper()

    if player_coordinates == 'q' or player_coordinates == "Q":       # ???how to use only one IF to break main and secondary loop together???
        print("Good bye.")
        break
    
    coordinates = False
    while coordinates == False:
        try:
            player_coordinates = list_of_coordinates(player_coordinates)
            coordinates = True
        except:
            player_coordinates = (input("Please enter coordinates in right format!: \n")).upper()

    player_turn(field, player_coordinates, player_symbol)    #store coordinates for horizontal_line method

    winner = Winner(symbol_in_row_to_win, field)
    check_draw_field = winner.fill_remain_fleld(player_symbol)
    check_draw_field = Winner(symbol_in_row_to_win, check_draw_field)
    check_draw_list = []

    
    # check horizontal line
    check_horizontal_line = winner.horizontal_line_one_line(player_coordinates[1], player_symbol)
    if check_horizontal_line == symbol_in_row_to_win:
        print(f"Player {player} is the winner. Congratulation!")
        break
        # check draw
    check_draw_horizontal = check_draw_field.horizontal_lines(player_symbol)
    if check_draw_horizontal == 0:
        check_draw_list.append(True)
    else:
        check_draw_list.append(False)

    # check vertical line
    check_vertical_line = winner.vertical_line_one_line(player_coordinates[0], player_symbol)
    if check_vertical_line == symbol_in_row_to_win:
        print(f"Player {player} is the winner. Congratulation!")
        break
        # check draw
    check_draw_vertical = check_draw_field.vertical_lines(player_symbol)
    if check_draw_vertical == 0:
        check_draw_list.append(True)
    else:
        check_draw_list.append(False)

    # check diagonal left to right
    check_diagonal_line = winner.diagonal_left_top_to_right_bottom(player_symbol)
    if check_diagonal_line == symbol_in_row_to_win:
        print(f"Player {player} is the winner. Congratulation!")
        break
        # check draw
    check_draw_diagonal_left = check_draw_field.diagonal_left_top_to_right_bottom(player_symbol)
    if check_draw_diagonal_left == 0:
        check_draw_list.append(True)
    else:
        check_draw_list.append(False)


    # check diagonal right to left
    check_diagonal_line = winner.diagonal_right_top_to_left_bottom(player_symbol)
    if check_diagonal_line == symbol_in_row_to_win:
        print(f"Player {player} is the winner. Congratulation!")
        break
        # check draw
    check_draw_diagonal_right = check_draw_field.diagonal_right_top_to_left_bottom(player_symbol)
    if check_draw_diagonal_right == 0:      
        check_draw_list.append(True)
    else:
        check_draw_list.append(False)

    if game_turn % 2 != 0:
        check_draw_player_one = check_draw_list
    else:    
        check_draw_player_two = check_draw_list
    
    # check draw
    if winner.draw_check(check_draw_player_one, check_draw_player_two) == True:
        print("It is draw!!")
        break
    
    game_turn += 1