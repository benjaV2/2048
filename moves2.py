

from settings import BOARD_RANGE, horizontal_moves, LEFT_MOVE, RIGHT_MOVE, UP_MOVE, DOWN_MOVE


def get_column(matrix, column_index):
    column = []
    for row in BOARD_RANGE:
        column.append(matrix[row][column_index])
    return column
        

def set_column(matrix, column, column_index):
    for row in BOARD_RANGE:
        matrix[row][column_index] = column[row]
    return matrix


def sum_tiles_left(row):
    for column in BOARD_RANGE[:-1]:
        if row[column] == row[column + 1]:
            row[column] *= 2
            row[column + 1] = 0
    return row
    

def move_tiles_left(row):
    left_row = []
    for column in BOARD_RANGE:
        if row[column] != 0:
            left_row.append(row[column])
    for i in BOARD_RANGE[:-len(left_row) if len(left_row) != 0 else len(BOARD_RANGE)]:
        left_row.append(0)
    return left_row
    
    
def sum_tiles_right(row):
    row = row[::-1]
    row = sum_tiles_left(row)
    return row[::-1]


def move_tiles_right(row):
    row = row[::-1]
    row = move_tiles_left(row)
    return row[::-1]


sums_moves = {LEFT_MOVE: sum_tiles_left, RIGHT_MOVE: sum_tiles_right,
              UP_MOVE: sum_tiles_left, DOWN_MOVE: sum_tiles_right}
moves = {LEFT_MOVE: move_tiles_left, RIGHT_MOVE: move_tiles_right,
         UP_MOVE: move_tiles_left, DOWN_MOVE: move_tiles_right}


def move_func(column, move):
    column = moves[move](column)
    column = sums_moves[move](column)
    column = moves[move](column)
    return column
    
    
def move_matrix(matrix, move):
    for index in BOARD_RANGE:
        if move in horizontal_moves:
            matrix[index] = move_func(matrix[index], move)
        else:
            column = get_column(matrix, index)
            column = move_func(column, move)
            matrix = set_column(matrix, column, index)
    return matrix


def equals_matrices(matrix, copy):
    for row in BOARD_RANGE:
        for column in BOARD_RANGE:
            if matrix[row][column] != copy[row][column]:
                return False
    return True


def check_move(matrix, move):
    matrix_copy = [row[:] for row in matrix]
    matrix_copy = move_matrix(matrix_copy, move)
    return not equals_matrices(matrix_copy, matrix)

