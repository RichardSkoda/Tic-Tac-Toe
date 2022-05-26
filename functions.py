def show_playground(field=[]):                        
        """Printing playground."""
        for lines in field:                                      
            for line in lines:
                print(line, end=" ")                              # end=" " - print whole list to one line. Default ending is \n


def player_turn(field, player_coordinates, player_symbol):
    """Place player one' symbol 'X' to playground."""
    while player_coordinates:
        try:                                                            # try if coordinates are in playground. If not, than exception
            coordinate_x = ord((player_coordinates[0])) - 64                  # convert upper letter to index of field list
            coordinate_y = int(player_coordinates[1]) +1
            if field[coordinate_y][coordinate_x] == '_':
                field[coordinate_y][coordinate_x] = player_symbol
                player_coordinates = None                               # exit loop if coordinates are OK
                show_playground(field)
            else:
                player_coordinates = list_of_coordinates((input(f"Coordinates {player_coordinates} are occupied. Please choose empty ones: ")).upper())
                
        except:
            show_playground(field)
            print("\nCoordinates are out of playground. Look at playground carefully!")
            player_coordinates = list_of_coordinates((input("Please choose new coordinates: \n")).upper())


def list_of_coordinates(coordinates):
    """Make a list of axis_x and axis_y coordinates."""
    list_of_coordinates = []
    for char in coordinates:
        list_of_coordinates.append(char)
    coordinate_y = "".join(list_of_coordinates[1:3])
    list_of_coordinates[1:3] = [int(coordinate_y)]
    return list_of_coordinates

def quit_game(player_coordinates):
    """Quit game if 'q' is entered."""
    if player_coordinates == 'q' or player_coordinates == "Q":       # ???how to use only one IF to break main and secondary loop together???
        print("Good bye.")
        return                  # what ot return to break loop where this function is?????