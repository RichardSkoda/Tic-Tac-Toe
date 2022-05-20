'''
     

    # check draw player one
    check_draw_field = winner.fill_remain_fleld(player_one_symbol)
    check_draw = winner.diagonal_left_top_to_right_bottom(player_one_symbol)
    if symbol_in_row_to_win == check_draw:
        continue
    else:
        check_draw_player_one = False
'''
'''
     # check draw player one
    check_draw_field = winner.fill_remain_fleld(player_two_symbol)
    check_draw = winner.diagonal_left_top_to_right_bottom(player_two_symbol)
    if symbol_in_row_to_win == check_draw:
        continue
    else:
       check_draw_player_two = False

    # check draw
    if winner.draw_check(check_draw_player_one, check_draw_player_two) == True:
        print("It is draw!!")
        break
    '''