import random
import math
from typing import List, Tuple, Optional
from enum import Enum

class State(Enum):
    DRAW = 0
    OVER = 1
    ONGOING = 2

class Board():
    def __init__(self):
        self.grid = [' '] * 9 # The game board
        self.turn = 'X' #Who's turn is it?
        self.game_state = State.ONGOING 
        self.winner = '' 
        self.moves_played = [] 
        self.is_maximizer = True # Useful for 

    def swap_turn(self) -> None:
        if self.turn == 'X':
            self.turn = 'O'
            self.maximizer = not self.is_maximizer
        elif self.turn == 'O':
            self.turn = 'X'
            self.maximizer = not self.is_maximizer
        else:
            raise ValueError(f"Oh god how did we end up here, self.turn is {self.turn}")


    def get_possible_moves(self) -> List[int] :
        return [i for i in range(9) if self.grid[i] == ' ']

    def make_move(self, move: int) -> None:
        if move not in self.get_possible_moves():
            raise ValueError("Not a valid move nerd!!")
        self.grid[move] = self.turn
        self.moves_played.append(move)
        self.game_state = self.get_game_state()
        self.swap_turn()

    def get_game_state(self) -> State:
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.grid[condition[0]] == self.grid[condition[1]] == self.grid[condition[2]] != ' ':
                self.winner = self.grid[condition[0]]
                return State.OVER
        if ' ' not in self.grid:
            return State.DRAW
        else:
            return State.ONGOING

    def get_winner(self) -> str:
        return self.winner 

    def undo(self) -> None:
        last_move = self.moves_played.pop()
        self.grid[last_move] = ' '
        self.swap_turn()

    # Function to draw the game board
    def draw_board(self):
        row1 = "| {} | {} | {} |".format(self.grid[0], self.grid[1], self.grid[2])
        row2 = "| {} | {} | {} |".format(self.grid[3], self.grid[4], self.grid[5])
        row3 = "| {} | {} | {} |".format(self.grid[6], self.grid[7], self.grid[8])
        print(row1)
        print(row2)
        print(row3)
    
def make_random_best_move(board) -> None:
    if board.is_maximizer:
        bestScore = -math.inf
    else:
        bestScore = math.inf

    bestMove = []
    for move in board.get_possible_moves():
        board.make_move(move)
        score = minimax(board)
        board.undo()
        if board.is_maximizer & (score >= bestScore):
            bestScore = score
            bestMove.append((move, score))
        elif (not board.is_maximizer) & (score <= bestScore):
            bestScore = score
            bestMove.append((score, move))
    assert bestMove is not []
    bestMove = [move for move, score in bestMove if score == bestScore ]
    bestMove = random.choice(bestMove)
    board.make_move(bestMove)

def minimax(board: Board) -> int:
    if (board.game_state is State.DRAW):
        return 0
    elif (board.game_state is State.OVER):
        return 1 if board.get_winner() is board.is_maximizer else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(board))
        board.undo()

    return max(scores) if board.is_maximizer else min(scores)

def play_game():
    board = Board()
    while board.game_state == State.ONGOING:
        make_best_move(board)
        board.draw_board()
        print("__________________")
    print("done!")
    return board


    

# Check if the game has ended
# def check_winner(board) -> Tuple[bool, int] :
#     win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
#                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                       (0, 4, 8), (2, 4, 6)]

#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
#             if board[condition[0]] == "X":
#                 return (True, 1)
#             elif board[condition[0]] == "O":
#                 return (True, -1)
#     if ' ' not in board:
#         return (True, 0)

#     return (False, 0)



    

    



# # Function to make a move
# def make_move(move, board, player_turn):
#     if player_turn % 2 == 0:
#         marker = 'X'
#     else:
#         marker = 'O'
#     if board[move] != ' ':
#         raise IndexError("move played in `make_move` must be on an empty square")
#     board[move] = marker

# # Check if the game has ended
# def check_winner(board) -> Tuple[bool, int] :
#     win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
#                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                       (0, 4, 8), (2, 4, 6)]

#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
#             if board[condition[0]] == "X":
#                 return (True, 1)
#             elif board[condition[0]] == "O":
#                 return (True, -1)
#     if ' ' not in board:
#         return (True, 0)

#     return (False, 0)

# def generate_random_game() -> List[int]:
#     available_moves : List[int] = list(range(0,9))
#     played_moves : List[int] = []
#     board : List[str] = [' ' for _ in range(9)]
#     for turn in range(0,9):
#         if turn > 4:
#             if check_winner(board):
#                 break
#         move = random.choice(available_moves)
#         available_moves.remove(move)
#         make_move(move, board, turn)
#         played_moves.append(move)
#     return played_moves


# """
# nodes of the tree are game states
# edges are moves
# Take in current board state, calculate all possible other board states from there.
# When you reach a leaf, if you win, the leaf is +1, if draw 0, if loss -1
# propagate the scores up to each node and pick the path with the highest score

# [0|X|X]
# [ |0|X]
# [ | | ]<-

# """

    







# # Main game loop
# player_turn = True
# while True:
#     move_sequence = []
#     draw_board()
#     print("Player 1's Turn" if player_turn else "Player 2's Turn")
#     
#     while True:
#         try:
#             move = int(input("Enter your move (0-8): "))
#             move_sequence.append(move)
#         except ValueError:
#             continue
#         if 0 <= move <= 8:
#             if make_move(move):
#                 break

#     winner = check_winner()
#     if winner:
#         draw_board()
#         if winner == 'Draw':
#             print("It's a draw.")
#         else:
#             print("Player {} wins!".format('1' if winner == 'X' else '2'))
#         break
#     player_turn = not player_turn


