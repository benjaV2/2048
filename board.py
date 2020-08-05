import random
from moves2 import move_matrix, check_move
from settings import BOARD_RANGE, BOARD_SIZE, reg_weight, uniq_weight,\
    tile_value_reg, tile_value_uniq, WIN_VALUE, valid_moves


class GameBoard:
    def __init__(self):
        self.matrix = [[0 for i in BOARD_RANGE] for i in BOARD_RANGE]
        self.insert_new_tile()
        
    def random_place(self):
        row = random.randrange(BOARD_SIZE)
        column = random.randrange(BOARD_SIZE)
        return row, column
        
    def random_tile(self):
        sed = random.randrange(reg_weight + uniq_weight)
        tile = tile_value_reg if sed < reg_weight else tile_value_uniq
        return tile
        
    def insert_new_tile(self):
        row, column = self.random_place()
        while self.matrix[row][column] != 0:
            row, column = self.random_place()
        self.matrix[row][column] = self.random_tile()
        
    def print_board(self):
        for row in BOARD_RANGE:
            for column in BOARD_RANGE:
                _end = " " if column < BOARD_SIZE - 1 else "\n" 
                print(f'%{len(str(WIN_VALUE))}d' % self.matrix[row][column], end=_end)
                
    def check_valid_move_remaining(self):
        for move in valid_moves:
            if self.check_valid(move) is True:
                return True
        return False
        
    def check_win_condition(self):
        for row in BOARD_RANGE:
            for column in BOARD_RANGE:
                if self.matrix[row][column] == WIN_VALUE:
                    return True
        return False
        
    def check_valid(self, user_move):
        if user_move not in valid_moves:
            return False
        return check_move(self.matrix, user_move)
        
    def move(self, user_move):
        self.matrix = move_matrix(self.matrix, user_move)
        self.insert_new_tile()
