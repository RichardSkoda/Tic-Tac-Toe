# check draw player two (try do this for each check)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    check_draw_diagonal_left = check_draw.diagonal_left_top_to_right_bottom(player_one_symbol) # pak do kazdeho checku dat i check na remizu
    if symbol_in_row_to_win == check_draw_diagonal_left:      # vytvorit list True a False. Kdyz pak budou vsechny False, bude remiza za jednoho hrace
        check_draw_player_one.append(False)
    else:
       check_draw_player_one.append(True)


# check draw player two
    check_draw_diagonal_right = check_draw.diagonal_left_top_to_right_bottom(player_two_symbol)
    if symbol_in_row_to_win == check_draw_diagonal_right:
        check_draw_player_one.append(False)
    else:
       check_draw_player_one.append(True)


 # check draw player two (try do this for each check)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    check_draw_diagonal_left = check_draw.diagonal_left_top_to_right_bottom(player_two_symbol) # pak do kazdeho checku dat i check na remizu
    if symbol_in_row_to_win == check_draw_diagonal_left:      # vytvorit list True a False. Kdyz pak budou vsechny False, bude remiza za jednoho hrace
        check_draw_player_two.append(False)
    else:
       check_draw_player_two.append(True)


# check draw player two
    check_draw_diagonal_right = check_draw.diagonal_left_top_to_right_bottom(player_two_symbol)
    if symbol_in_row_to_win == check_draw_diagonal_right:
        check_draw_player_two.append(False)
    else:
       check_draw_player_two.append(True)