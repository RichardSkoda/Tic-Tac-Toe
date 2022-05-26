# function code before shortening!!!!!!!!!!!! draw is not function

from playground import Tic_Tac_Toe as TTT
from winner import Winner
from functions import player_turn, show_playground
from functions import player_turn, list_of_coordinates


player_one_symbol = "X"
player_two_symbol = "O"

# set playground parameters
print("\n\nWelcome to Tic Tac Toe match!\n")
size_x = int(input("Please set size of axis x (max. 26): "))
size_y = int(input("Please set size of axis y (max. 99): "))
symbol_in_row_to_win = int(input("Please set how many symbols in row to win (3-5): "))

# make a playground
playground = TTT(size_x, size_y)                    # make an instance of Tic_Tac_Toe class
field = playground.game_field()


print("\nPlease enter coordinates like 'A3'.\n"
    "Enter 'q' for exit the game.\n")
show_playground(field)


while True:

    # player 1 turn
    player_1_coordinates = (input("\nPlayer one turn: \n")).upper()
    if player_1_coordinates[0] == "Q":               # ???how to use only one IF to break main and secondary loop together???
        print("Good bye.")
        break
    player_1_coordinates = list_of_coordinates(player_1_coordinates)
    player_turn(field, player_1_coordinates, player_one_symbol)    #store coordinates for horizontal_line method

    winner = Winner(symbol_in_row_to_win, field)
    check_draw_field = winner.fill_remain_fleld(player_one_symbol)
    check_draw = Winner(symbol_in_row_to_win, check_draw_field)
    check_draw_player_one = []      # make a list of draw check for each line check

    # check horizontal line
    check_horizontal_line = winner.horizontal_line_one_line(player_1_coordinates[1], player_one_symbol)
    if check_horizontal_line == symbol_in_row_to_win:
        print("Player one is the winner. Congratulation!")
        break
        # check draw player two
    check_draw_horizontal = check_draw.horizontal_lines(player_one_symbol)
    if check_draw_horizontal == 0:
        check_draw_player_one.append(True)
    else:
        check_draw_player_one.append(False)

    # check vertical line
    check_vertical_line = winner.vertical_line_one_line(player_1_coordinates[0], player_one_symbol)
    if check_vertical_line == symbol_in_row_to_win:
        print("Player one is the winner. Congratulation!")
        break
        # check draw player two
    check_draw_vertical = check_draw.vertical_lines(player_one_symbol)
    if check_draw_vertical == 0:
        check_draw_player_one.append(True)
    else:
        check_draw_player_one.append(False)

    # check diagonal left to right
    check_diagonal_line = winner.diagonal_left_top_to_right_bottom(player_one_symbol)
    if check_diagonal_line == symbol_in_row_to_win:
        print("Player one is the winner. Congratulation!")
        break
        # check draw player two (try do this for each check)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    check_draw_diagonal_left = check_draw.diagonal_left_top_to_right_bottom(player_one_symbol) # pak do kazdeho checku dat i check na remizu
    if check_draw_diagonal_left == 0:      # vytvorit list True a False. Kdyz pak budou vsechny False, bude remiza za jednoho hrace
        check_draw_player_one.append(True)
    else:
        check_draw_player_one.append(False)


    # check diagonal right to left
    check_diagonal_line = winner.diagonal_right_top_to_left_bottom(player_one_symbol)
    if check_diagonal_line == symbol_in_row_to_win:
        print("Player one is the winner. Congratulation!")
        break
        # check draw player two (try do this for each check)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    check_draw_diagonal_right = check_draw.diagonal_right_top_to_left_bottom(player_one_symbol) # pak do kazdeho checku dat i check na remizu
    if check_draw_diagonal_right == 0:      # vytvorit list True a False. Kdyz pak budou vsechny False, bude remiza za jednoho hrace
        check_draw_player_one.append(True)
    else:
        check_draw_player_one.append(False)
    

    # player 2 turn
    player_2_coordinates = (input("\nPlayer two turn: \n")).upper()
    if player_2_coordinates[0] == "Q":              # ???how to use only one IF to break main and secondary loop together???
        print("Good bye.")
        break
    player_2_coordinates = list_of_coordinates(player_2_coordinates)
    player_turn(field, player_2_coordinates, player_two_symbol)

    winner = Winner(symbol_in_row_to_win, field)
    check_draw_field = winner.fill_remain_fleld(player_two_symbol)
    check_draw = Winner(symbol_in_row_to_win, check_draw_field)
    check_draw_player_two = []      # make a list of draw check for each line check

    # check horizontal line
    check_horizontal_line = winner.horizontal_line_one_line(player_2_coordinates[1], player_two_symbol)
    if check_horizontal_line == symbol_in_row_to_win:
        print("Player two is the winner. Congratulation!")
        break
        # check draw player two
    check_draw_horizontal = check_draw.horizontal_lines(player_two_symbol)
    if check_draw_horizontal == 0:
        check_draw_player_two.append(True)
    else:
        check_draw_player_two.append(False)       # return True if conditions for draw

    # check vertical line
    check_vertical_line = winner.vertical_line_one_line(player_2_coordinates[0], player_two_symbol)
    if check_vertical_line == symbol_in_row_to_win:
        print("Player two is the winner. Congratulation!")
        break
        # check draw player two
    check_draw_vertical = check_draw.vertical_lines(player_two_symbol)
    if check_draw_vertical == 0:
        check_draw_player_two.append(True)
    else:
        check_draw_player_two.append(False)

    # check diagonal left to right
    check_diagonal_line = winner.diagonal_left_top_to_right_bottom(player_two_symbol)
    if check_diagonal_line == symbol_in_row_to_win:
        print("Player two is the winner. Congratulation!")
        break
        # check draw player two
    check_draw_diagonal_left = check_draw.diagonal_left_top_to_right_bottom(player_two_symbol)
    if check_draw_diagonal_left == 0:
        check_draw_player_two.append(True)
    else:
        check_draw_player_two.append(False)
           
    # check diagonal right to left
    check_diagonal_line = winner.diagonal_right_top_to_left_bottom(player_two_symbol)
    if check_diagonal_line == symbol_in_row_to_win:
        print("Player two is the winner. Congratulation!")
        break
        # check draw player two
    check_draw_diagonal_right = check_draw.diagonal_right_top_to_left_bottom(player_two_symbol)
    print(check_draw_diagonal_right)
    if check_draw_diagonal_right == 0:
        check_draw_player_two.append(True)
    else:
        check_draw_player_two.append(False)

            

    # check draw    predelat podle druhe casti kazdeho checku!!!!! kontrolovat list Flase/True
    if winner.draw_check(check_draw_player_one, check_draw_player_two) == True:
        print("It is draw!!")
        break

