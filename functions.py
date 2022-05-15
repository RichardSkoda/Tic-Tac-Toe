def show_playground(field=[]):                        
        """Printing playground."""
        for lines in field:                                      
            for line in lines:
                print(line, end=" ")                              # end=" " - print whole list to one line. Default ending is \n



def player_1(field, player_1_coordinates):
    """Place player one' symbol 'X' to playground."""
    while player_1_coordinates:
        try:
            if player_1_coordinates == 'q' or player_1_coordinates == "Q":       # ???how to use only one IF to break main and secondary loop together???
                print("Good bye.")
                break
            coordinate_x = ord((player_1_coordinates[0])) - 64                  # convert upper letter to index of filed list
            coordinate_y = int(player_1_coordinates[1]) +1
            if field[coordinate_y][coordinate_x] == '_':
                field[coordinate_y][coordinate_x] = 'X'
                player_1_coordinates = None
                show_playground(field)
            else:
                player_1_coordinates = list_of_coordinates((input(f"Coordinates {player_1_coordinates} are occupied. Please choose empty ones: ")).upper())
                

        except:
            show_playground(field)
            print("\nCoordinates are out of playground. Look at playground carefully!")
            player_1_coordinates = list_of_coordinates((input("Please choose new coordinates: \n")).upper())



def player_2(field, player_2_coordinates):
    """Place player one' symbol 'O' to playground."""
    while player_2_coordinates:
        if player_2_coordinates == 'q' or player_2_coordinates == "Q":
            print("Good bye.")
            break
        try:
            coordinate_x = ord((player_2_coordinates[0])) - 64                  
            coordinate_y = int(player_2_coordinates[1]) +1
            if field[coordinate_y][coordinate_x] == '_':
                field[coordinate_y][coordinate_x] = 'O'
                player_2_coordinates = None
                show_playground(field)
            else:
                player_2_coordinates = list_of_coordinates((input(f"Coordinates {player_2_coordinates} are occupied. Please choose empty ones: ")).upper())

        except:
            show_playground(field)
            print("\nCoordinates are out of playground. Look at playground carefully!")
            player_2_coordinates = list_of_coordinates((input("Please choose new coordinates: \n")).upper())


def list_of_coordinates(coordinates):
    """Make a list of axis_x and axis_y coordinates."""
    list_of_coordinates = []
    for char in coordinates:
        list_of_coordinates.append(char)
    coordinate_y = "".join(list_of_coordinates[1:3])
    list_of_coordinates[1:3] = [coordinate_y]
    return list_of_coordinates
