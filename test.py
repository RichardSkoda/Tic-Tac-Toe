winner = Winner(symbol_in_row_to_win, field)
    check_horizontal_line = winner.horizontal_line(coordinates[1], player_one_symbol)
    print(check_horizontal_line)
    if check_horizontal_line == symbol_in_row_to_win:
        print("Player one is the winner. Congratulation!")
        break

    

