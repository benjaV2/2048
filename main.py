

# main file for user interaction 

from board import GameBoard
from settings import DOWN_MOVE, UP_MOVE, LEFT_MOVE, RIGHT_MOVE


game_board = GameBoard()
game_board.print_board()
while game_board.check_valid_move_remaining() and not game_board.check_win_condition():
    user_move = input(f"Enter move ({LEFT_MOVE}/{DOWN_MOVE}/{UP_MOVE}/{RIGHT_MOVE}) : ")
    while not game_board.check_valid(user_move):
        user_move = input(f"Move invalid. Enter new move ({LEFT_MOVE}/{DOWN_MOVE}/{UP_MOVE}/{RIGHT_MOVE}) : ")
    game_board.move(user_move)
    game_board.print_board()
    
if game_board.check_win_condition():
    print("congratulations you Won!")
else:
    print("No Moves Left.")

