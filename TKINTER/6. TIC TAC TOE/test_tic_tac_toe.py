# TEST TIC TAC TOE GAME WITH TERMINAL APPROACH
# Santiago Garcia Arango
# MLH2021

# My own imports
import tic_tac_toe as ttt

class PlayGame:
    def __init__(self):
        self.game = ttt.TicTacToe()
        self.main_loop()

    def main_loop(self):
        while self.game.check_winner() == 0:
            self.get_players_move()

        winner = self.game.current_player
        print("\n\nTHE WINNER IS: ", winner, "!!!!\n\n")

    def get_players_move(self):
        position = str(input("PLAY MOVE IN FORMAT \"xx\":"))
        position = list(position)
        # print(position)
        self.game.move([int(position[0]), int(position[1])])


if __name__ == "__main__":
    G1 = PlayGame()
