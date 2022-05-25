import numpy as np

matrix = [['_', 'X', '_', '_', '_'], ['_', '_', 'X', '_', '_'], ['_', '_', '_', 'X', '_'], ['_', '_', '_', '_', 'X'], ['_', '_', 'X', '_', '_']]
matrix = np.array(matrix)
a = matrix.shape[0]
diagonals_left_to_right = [np.diag(matrix, k=i).tolist() for i in range(-a+1,a)]
print(diagonals_left_to_right)

symbol_in_row = 0

for diagonal in diagonals_left_to_right:
    if symbol_in_row == 3:
        break
    symbol_in_row = 0
    for place in diagonal:
        if place == 'X':
            symbol_in_row += 1
        elif place != 'X':
            symbol_in_row = 0
        if symbol_in_row == 3:
            break
                

print(symbol_in_row)