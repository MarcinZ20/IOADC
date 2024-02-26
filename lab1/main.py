import random
import numpy as np

from typing import List, Tuple
from easyAI import Negamax
from easyAI.Player import AI_Player
from easyAI.TwoPlayerGame import TwoPlayerGame


class TicTacDoh(TwoPlayerGame):
    """ For now, this is a simple implementation of the Tic–Tac-Doh game.

    Args:
        TwoPlayerGame (base class): Base class for two-player games. It provides a simple interface for the game to be played.
    """

    def __init__(self, players: List) -> None:
        """Initializes the game with the players and the board.

        Args:
            players (List): List of players.
        """
        self.board = np.zeros(9, np.uint8)
        self.players = players
        self.current_player = 1

    def possible_moves(self) -> np.ndarray:
        """Returns the possible moves for the current player.

        Returns:
            np.ndarray: Array of possible moves.
        """
        return [i + 1 for i, v in enumerate(self.board) if v == 0]

    def make_move(self, move: int) -> None:
        """Makes a move on the board.

        Args:
            move (int): The move to be made.
        """
        moves = [True, False]
        weights = [0.8, 0.2]

        move_is_success = random.choices(moves, weights, k=1)[0]

        if move_is_success:
            self.board[move - 1] = self.current_player

    def is_over(self) -> bool:
        """Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.check_win() or len(self.possible_moves()) == 0

    def check_win(self) -> bool:
        """Checks if the current player has won the game.

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        # FIXME: Should be from opponents perspective I think .. not sure though

        board = self.board.reshape(3, 3)
        target_array = [self.current_player for _ in range(3)]

        for row in range(3):
            if all(np.equal(board[row, :], target_array)):
                return True
        
        for col in range(3):
            if all(np.equal(board[:, col], target_array)):
                return True
            
        if all(np.equal(board.diagonal(), target_array)) or all(np.equal(np.fliplr(board).diagonal, target_array)):
            return True
        
        return False

    def scoring(self) -> int:
        """Returns the score of the current player.

        Returns:
            int: The score of the current player.
        """
        # FIXME: This is not working
        return -100 if self.check_win else 0
    
    def play(self) -> Tuple[int, List[int]]:
        """Starts the game.

        Returns:
            Tuple[int, List[int]]: The winner and the board.
        """
        
        print("\nPlayer 1: X\nPlayer 2: O")
        print("=====================\n")

        while not self.is_over():
            move = self.get_move()
            self.play_move(move)
            self.show()

        print("Player", self.current_player, "wins")
        return (self.current_player, self.board)
    
    def show(self) -> None:
        """Prints the board.
        """
        board = ['X' if i == 1 else 'O' if i == 2 else ' ' for i in self.board]

        a = (' ___' *  3 )
        b = (f'| {board[0]} | {board[1]} | {board[2]} |')
        c = (f'| {board[3]} | {board[4]} | {board[5]} |')
        d = (f'| {board[6]} | {board[7]} | {board[8]} |')
        e = ('|---+---+---|')
        f = (' ---' *  3 )

        print("MOVE BY PLAYER: ", self.opponent_index) # Opponent because we call show after change of the current_player
        print('\n'.join((a, b, e, c, e, d, f)))
        print('\n\n')


class Test:
    
    def __init__(self, number_of_games: int) -> None:
        self.number_of_games = number_of_games
        self.ai_algo = Negamax(6)
        self.scores = []

    def start(self):
        # TODO: Make the players switch between each other after each game
        # TODO: Switch max_depth between 3 and 6 for each game
        player_1 = AI_Player(self.ai_algo)
        player_2 = AI_Player(self.ai_algo)

        for _ in range(self.number_of_games):
            game = TicTacDoh(players=[player_1, player_2])
            score = game.play()
            self.scores.append(score)

if __name__ == "__main__":
    test = Test(1).start()