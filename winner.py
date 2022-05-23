from playground import Tic_Tac_Toe as TTT
import numpy as np

class Winner():
    """Class chose who is the winner of Tic Tac Toe."""

    def __init__(self, row_to_win, field):
        """Initialize the game aspects.."""
        self.playground = TTT(self)
        self.field = field
        self.row_to_win = row_to_win

    def horizontal_line_one_line(self, line_index, symbol):
        """Check particular horizontal line."""
        symbol_in_row = 0
        for place in self.field[line_index + 1]:            # +1 beacause first line is line with horizontal coordinates (A B C ...)
            if symbol_in_row == self.row_to_win:
                break
            if place == symbol:
                symbol_in_row += 1
            elif place != symbol:                           # I used elif instead of else because place can be '_' or other symbol 'X' or 'Y'
                symbol_in_row = 0
        
        return symbol_in_row

    def horizontal_lines(self, symbol):         # have to make a list of True/Flase each item is one line and retrum thhis list to check
        """Check all horizontal lines."""
        for horizontal in self.fied:



    def vertical_line_one_line(self, column_index, symbol):
        """Check particular vertical line."""
        symbol_in_row = 0
        
        for line in self.field:
            if symbol_in_row == self.row_to_win:
                break
            if line[ord(column_index) - 64] == symbol:          # have to convert letter coordinate to number
                symbol_in_row += 1
            elif line[ord(column_index) - 64] != symbol:
                symbol_in_row = 0

        return symbol_in_row

    def vertical_lines(self, symbol):
        """Check all horizontal line."""
        for vertical in self.field:
            for place in vertical:
                symbol_in_row = 0
                if symbol_in_row != self.row_to_win:
                    break
                if place == symbol:
                    symbol_in_row += 1
                elif place != symbol:
                    symbol_in_row = 0
        return symbol_in_row

    def diagonal_left_top_to_right_bottom(self, symbol):
        """Check particular diagonal lines."""
        symbol_in_row = 0
        
        matrix = self._matrix_only_play_fields()
        # from stack overflow- find how it is working and do the same for another diagonals
        matrix = np.array(matrix)
        matrix = np.flipud(matrix)  # flipud make matrix in mirror shape, so diagonals are oposit 
        a = matrix.shape[0]
        diagonals_left_to_right = [np.diag(matrix, k=i).tolist() for i in range(-a+1,a)]

        # diagonal lef to right check
        for diagonal in diagonals_left_to_right:
            for place in diagonal:
                symbol_in_row = 0
                if symbol_in_row == self.row_to_win:
                    break
                if place == symbol:
                    symbol_in_row += 1
                elif place != symbol:
                    symbol_in_row = 0
        return symbol_in_row

    def diagonal_right_top_to_left_bottom(self, symbol):
        """Check particular diagonal lines."""
        symbol_in_row = 0
        
        matrix = self._matrix_only_play_fields()
        # from stack overflow- find how it is working and do the same for another diagonals
        matrix = np.array(matrix)
        a = matrix.shape[0]
        diagonals_right_to_left = [np.diag(matrix, k=i).tolist() for i in range(-a+1,a)]

        # diagonal lef to right check
        for diagonal in diagonals_right_to_left:
            symbol_in_row = 0
            for place in diagonal:
                if symbol_in_row == self.row_to_win:
                    break
                if place == symbol:
                    symbol_in_row += 1
                elif place != symbol:
                    symbol_in_row = 0
        return symbol_in_row

    def _matrix_only_play_fields(self):
        """Make playground only with fields for player's symbols.."""
        field_without_axisx_coordinates = self.field[1:]
        matrix = []
        for line in field_without_axisx_coordinates:
            line = line[1:]
            matrix.append(line)

        return matrix

    def draw_check(self, player_one_draw, player_two_draw):
        """Fill free places by given symbol."""
        if all(player_one_draw) == True and all(player_two_draw) == True:
            return True
        else:
            return False

    def fill_remain_fleld(self, symbol):
        """Fill free places by given symbol."""
        matrix = self._matrix_only_play_fields()
        matrix = np.array(matrix)
        matrix = np.char.replace(matrix, '_', symbol, count=None)
        print(matrix)

        return matrix