from playground import Tic_Tac_Toe as TTT

class Winner():
    """Class chose who is the winner of Tic Tac Toe."""

    def __init__(self, row_to_win, field):
        """Initialize the game aspects.."""
        self.playground = TTT()
        self.field = field
        self.row_to_win = row_to_win

    def horizontal_line(self, line_index, symbol):
        """Check particular horizontal line."""
        symbol_in_row = 0
        for place in self.field[line_index + 1]:            # +1 beacause first line is line with horizontal coordinates (A B C ...)
            if symbol_in_row == self.row_to_win:
                break
            if place == symbol:
                symbol_in_row += 1
            elif place != symbol:
                symbol_in_row = 0
        
        return symbol_in_row


    def vertical_line(self, column_index, symbol):
        """Check particular vertical line."""
        symbol_in_row = 0
        # budu muset z funkce player turn list koordinatu a tahat to y listu
            