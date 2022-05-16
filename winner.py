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
            elif place != symbol:                           # I used elif instead of else because place can be '_' or other symbol 'X' or 'Y'
                symbol_in_row = 0
        
        return symbol_in_row


    def vertical_line(self, column_index, symbol):
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

    def diagonal_left_top_to_right_bottom(self, line_index, column_index, symbol):
        """Check particular diagonal lines."""
        symbol_in_row = 0
        
        # diagonal left to right making a list of coordinates
        diagonal_left_to_right = []

        # diagonal from one place to right down
        for place in self.field: 
            count = 0
            try:        # I looking for out of index
                coordinates = (ord(column_index) - 64 + count), [line_index + count]
                diagonal_left_to_right.append(coordinates)
                count += 1
            except:
                continue
        
        # diagonal from one place to left up
        for place in self.field: 
            count = 0
            try:
                coordinates = (ord(column_index) - 64 - 1 - count), [line_index + count]  # -1 because I add original coordinates to list already
                diagonal_left_to_right.append(coordinates)
                count += 1
            except:
                continue
        print(diagonal_left_to_right)      # !!! tady mam ulozeny list z tuples !!!!

        # diagonal lef to right check
        for coordinates in sorted(diagonal_left_to_right):
            print(coordinates)      # !!!! toto mam ulozen tuple  !!!!!
            if symbol_in_row == self.row_to_win:
                break
            if self.field[coordinates[1]][coordinates[0]] == symbol:
                symbol_in_row += 1
            elif self.field[coordinates[1]][coordinates[0]] != symbol:
                symbol_in_row = 0

        return symbol_in_row


    def diagonal_right_top_to_left_bottom(self, line_index, column_index, symbol):
        """Check particular diagonal lines."""
        symbol_in_row = 0            

        # diagonal right to left

        diagonal_right_to_left = []
        # diagonal from one place to left down
        for place in self.field: 
            count = 0
            try:
                # puvodni - coordinates = [self.field[ord(column_index) - 64 - count], [line_index + count]]
                coordinates = (ord(column_index) - 64 - count), [line_index + count]
                diagonal_right_to_left.append(coordinates)
                count += 1
            except:
                continue
        
        # diagonal from one place to right up
        for place in self.field: 
            count = 0
            try:
                coordinates = (ord(column_index) - 64 - 1 + count), [line_index + count]  # -1 because I add original coordinates to list already
                diagonal_right_to_left.append(coordinates)
                count += 1
            except:
                continue

        # diagonal right to left check
        for coordinates in sorted(diagonal_right_to_left):
            if symbol_in_row == self.row_to_win:
                break
            if self.field[coordinates[1]][coordinates[0]] == symbol:
                symbol_in_row += 1
            elif self.field[coordinates[1]][coordinates[0]] != symbol:
                symbol_in_row = 0

        return symbol_in_row
            




'''

            # how to check diagonal
            # diagonal from one place to left down
            try:
                if self.field[ord(column_index) - 64 - count][line_index + count] == symbol:
                    symbol_in_row += 1
                elif self.field[ord(column_index) - 64 - count][line_index + count] != symbol:
                    symbol_in_row = 0
                count += 1
            except:
                continue
            
            # diagonal from one place to right up
            try:
                if self.field[ord(column_index) - 64 + count][line_index - count] == symbol:
                    symbol_in_row += 1
                elif self.field[ord(column_index) - 64 - count][line_index - count] != symbol:
                    symbol_in_row = 0
                count += 1
            except:
                continue

'''



    