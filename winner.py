import numpy as np

class Winner():
    """Class chose who is the winner of Tic Tac Toe."""

    def __init__(self, row_to_win, field):
        """Initialize the game aspects.."""
        self.field = field
        self.row_to_win = row_to_win

    def horizontal_line_one_line(self, line_index, symbol):     # I can use only horizontal_lines method, but this one checks only one line
        """Check particular horizontal line."""
        symbol_in_row = 0
        for place in self.field[line_index + 1]:            # +1 beacause first line is line with horizontal coordinates (A B C ...)
            if symbol_in_row == self.row_to_win:
                break
            if place == symbol:
                symbol_in_row += 1
            elif place != symbol:                           # I used elif instead of else because place can be '_' or other symbols 'X' or 'Y'
                symbol_in_row = 0
        
        return symbol_in_row

    def vertical_line_one_line(self, column_index, symbol):     # I can use only vertical_lines method, but this one checks only one line
        """Check particular vertical line."""                   # I can reduce code more than 20 lines, but I decided to leave it in that way
        symbol_in_row = 0
        for line in self.field:
            if symbol_in_row == self.row_to_win:
                break
            if line[ord(column_index) - 64] == symbol:          # have to convert letter coordinate to number
                symbol_in_row += 1
            elif line[ord(column_index) - 64] != symbol:
                symbol_in_row = 0

        return symbol_in_row

    def horizontal_lines(self, symbol):         
        """Check all horizontal lines."""
        field = self._matrix_only_play_fields()
        field = np.array(field)
        symbol_in_row = self._check_lines(symbol, field)
        return symbol_in_row

    def vertical_lines(self, symbol):          
        """Check all horizontal line."""
        field = self._matrix_only_play_fields()
        field = np.array(field)
        field_switched_axis = field.T       # .T attribute make lists from vertical lines in matrix
        symbol_in_row = self._check_lines(symbol, field_switched_axis)
        return symbol_in_row

    def diagonal_left_top_to_right_bottom(self, symbol):
        """Check particular diagonal lines."""
        
        matrix = self._matrix_only_play_fields()
        # from stack overflow
        matrix = np.array(matrix)
        matrix = np.flipud(matrix)  # flipud make matrix in mirror shape, so diagonals are oposit 
        a = matrix.shape[0]
        diagonals_left_to_right = [np.diag(matrix, k=i).tolist() for i in range(-a+1,a)]    # make diagonals of the matrix
        # diagonal lef to right check
        symbol_in_row = self._check_lines(symbol, diagonals_left_to_right)
        return symbol_in_row

    def diagonal_right_top_to_left_bottom(self, symbol):
        """Check particular diagonal lines."""
        
        matrix = self._matrix_only_play_fields()
        matrix = np.array(matrix)
        a = matrix.shape[0]
        diagonals_right_to_left = [np.diag(matrix, k=i).tolist() for i in range(-a+1,a)]
        # diagonal lef to right check
        symbol_in_row = self._check_lines(symbol, diagonals_right_to_left)
        return symbol_in_row
        
    def _check_lines(self, symbol, field=[]):
        """Code to check lines in field."""
        symbol_in_row = 0
        for line in field:
            if symbol_in_row == self.row_to_win:
                    break
            symbol_in_row = 0
            for place in line:
                if place == symbol:
                    symbol_in_row += 1
                elif place != symbol:
                    symbol_in_row = 0
                if symbol_in_row == self.row_to_win:
                    break

        return symbol_in_row

    def _matrix_only_play_fields(self):
        """Make playground with only places for player's symbols."""
        field_without_axisx_coordinates = self.field[1:]
        matrix = []
        for line in field_without_axisx_coordinates:
            line = line[1:]
            matrix.append(line)

        return matrix

    def draw_check(self, player_one_draw, player_two_draw):
        """Fill free places in playground by given symbol."""
        if all(player_one_draw) == True and all(player_two_draw) == True:
            return True
        else:
            return False

    def fill_remain_fleld(self, symbol):
        """Fill free places by given symbol."""
        matrix = np.array(self.field)
        matrix = np.char.replace(matrix, '_', symbol, count=None)

        return matrix