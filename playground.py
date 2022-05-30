class Tic_Tac_Toe:
    """Make a Tic Tac Toe game"""

    def __init__(self, axis_x=5, axis_y=5):
        """Initialize game attributes."""
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.playground = []

    def game_field(self):
        """Make a playground."""
        self._line_1()
        self._rest_lines()
        return self.playground
        #self._print_playground()

    def _line_1(self):
        """Define the first line of coordinates to playground.""" 
        line_1 = ['   ', ]
        for place in range(self.axis_x):
            line_1.append(chr(place + 65))                                  # convert x coordinate to letter by ascii
        line_1.append("\n")
        self.playground.append(line_1)
        
    def _rest_lines(self):
        """Make all line of playground except the first one."""
        count = 0
        while count <= self.axis_y - 1:
            rest_lines = []
            if count < 10:
                one_char_y_coordinate = (f'{count} ')                        # have to add space to 0-9 numbers
                rest_lines.append(one_char_y_coordinate)                     # first number of axis y of playground (0)
            else:
                rest_lines.append(count)                            
            for position in range(self.axis_x):
                rest_lines.append("_")                            # add playground field                                
            rest_lines.append("\n")                           # add new line as final symbol in list of fields
            self.playground.append(rest_lines)                    # add whole line to playground
            count += 1

    def show_playground(self):                       
        """Printing playground."""
        for lines in self.playground:                                       
            for line in lines:
                print(line, end=" ")                              # end=" " - print whole list to one line. Default ending is \n