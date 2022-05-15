def list_of_coordinates(coordinates):
    """Make a list of axis_x and axis_y coordinates."""
    list_of_coordinates = []
    for char in coordinates:
        list_of_coordinates.append(char)
    coordinate_y = "".join(list_of_coordinates[1:3])
    list_of_coordinates[1:3] = [coordinate_y]
    return list_of_coordinates