# BUILD TIC-TAC-TOE  GAME FROM SCRATCH
# Santiago Garcia Arango
# MLH2021

import numpy as np


class TicTacToe:
    def __init__(self):
        self.restart_board()
        self.current_player = 1

    def restart_board(self):
        self.board = np.zeros((3, 3))
        # print(self.board)

    def move(self, position):
        valid_position = self.board[position[0], position[1]]
        if valid_position > 0:
            print("Invalid move")
            return False

        # Player's 1 turn
        if (self.current_player == 1):
            self.board[position[0], position[1]] = 1
            winner_status = self.check_winner()
            print(winner_status)
            print(self.board)
            if winner_status > 0:
                return True
            else:
                self.current_player = 2
                return True

        # Player's 2 turn
        if (self.current_player == 2):
            self.board[position[0], position[1]] = 2
            winner_status = self.check_winner()
            print(winner_status)
            print(self.board)
            if winner_status > 0:
                return True
            else:
                self.current_player = 1
                return True

    def check_winner(self):
        # Check if player 1 wins
        for i in range(3):
            # Check vertical lines
            if (self.board[0, i] == self.board[1, i] and self.board[1, i] == self.board[2, i] and self.board[2, i] == 1):
                return 1

            # Check horizontal lines
            if (self.board[i, 0] == self.board[i, 1] and self.board[i, 1] == self.board[i, 2] and self.board[i, 2] == 1):
                return 1

            # Check main diagonal
            if (self.board[0, 0] == self.board[1, 1] and self.board[1, 1] == self.board[2, 2] and self.board[2, 2] == 1):
                return 1

            # Check secundary diagonal
            if (self.board[0, 2] == self.board[1, 1] and self.board[1, 1] == self.board[2, 0] and self.board[2, 0] == 1):
                return 1

        # Check if player 2 wins
        for i in range(3):
            # Check vertical lines
            if (self.board[0, i] == self.board[1, i] and self.board[1, i] == self.board[2, i] and self.board[2, i] == 2):
                return 2

            # Check horizontal lines
            if (self.board[i, 0] == self.board[i, 1] and self.board[i, 1] == self.board[i, 2] and self.board[i, 2] == 2):
                return 2

            # Check main diagonal
            if (self.board[0, 0] == self.board[1, 1] and self.board[1, 1] == self.board[2, 2] and self.board[2, 2] == 2):
                return 2

            # Check secundary diagonal
            if (self.board[0, 2] == self.board[1, 1] and self.board[1, 1] == self.board[2, 0] and self.board[2, 0] == 2):
                return 2

        # Check if there are NO more possible moves available
        total_moves = 0
        for i in range(3):
            for j in range(3):
                if self.board[i, j] > 0:
                    total_moves = total_moves + 1

        # If all moves are done, return 3 (which means that there was a tie)
        if total_moves == 9:
            return 3

        # If no one has won yet
        return 0


if __name__ == "__main__":
    # Hard computed test (check test_tic_tac_toe.py for test playing)
    b1 = TicTacToe()
    b1.move([0, 0])
    b1.move([1, 1])
    b1.move([2, 2])
    b1.move([0, 2])
    b1.move([2, 0])
    b1.move([1, 0])
    b1.move([2, 1])
