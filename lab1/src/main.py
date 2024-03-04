import random
import numpy as np
import time


from typing import List, Tuple
from easyAI import Negamax
from easyAI.Player import AI_Player
from easyAI.TwoPlayerGame import TwoPlayerGame


class TicTacDoh(TwoPlayerGame):
    """ For now, this is a simple implementation of the Tic–Tac-Doh game.

    Args:
        TwoPlayerGame (base class): Base class for two-player games. It provides a simple interface for the game to be played.
    """
    
    WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],  
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],  
        [1, 5, 9],
        [3, 5, 7],
    ]

    def __init__(self, players: List) -> None:
        """Initializes the game with the players and the board.

        Args:
            players (List): List of players.
        """
        self.board = np.zeros(9, np.uint8)
        self.players = players
        self.current_player = random.randint(1, 2)
        self.av_move_time = 0
        self.moves_number = 0

        print("First player: ", end="")
        print(self.current_player)

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
        return self.lose() or self.lose(player=self.current_player) or len(self.possible_moves()) == 0

    def lose(self, player=None) -> bool:
        """Checks if the current player has lost.
        
        Args:
            player (int, optional): The player to check. Defaults to None.
        """

        if player is None:
            player = self.opponent_index
        
        wins = [all([(self.board[c - 1] == player) for c in line]) for line in self.WIN_LINES]
        return any(wins)

    def scoring(self) -> int:
        """Returns the score of the current player.

        Returns:
            int: The score of the current player.
        """
        opp_won = self.lose()
        i_won = self.lose(player=self.current_player)

        if opp_won and not i_won:
            return -100
        if i_won and not opp_won:
            return 100
        return 0

    def winner(self):
        if self.lose(who=2):
            return "AI-1 Wins!"
        elif self.lose(who=1):
            return "AI-2 Wins!"
        return "Tie"
    
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
        print('Average move time: ', end='')
        print(round(self.av_move_time, 5))
        print('\n\n')

    def play(self) -> Tuple[int, List[int]]:
        """Starts the game.

        Returns:
            Tuple[int, List[int]]: The winner and the board.
        """
        
        print("\nPlayer 1: X\nPlayer 2: O")
        print("=====================\n")

        while not self.is_over():
            begin = time.time()
            move = self.get_move()
            end = time.time()
            new_time = end-begin
            old_av_time = self.av_move_time * self.moves_number
            self.moves_number += 1
            old_av_time += new_time
            self.av_move_time = old_av_time / self.moves_number

            self.play_move(move)
            self.show()

        return (self.opponent_index, self.board)

class Test:
    
    def __init__(self, number_of_games: int) -> None:
        self.number_of_games = number_of_games
        self.ai_algo = Negamax(3)
        self.scores = []

    def start(self):
        # TODO: Make the players switch between each other after each game - DONE
        # TODO: Switch max_depth between 3 and 6 for each game
        player_1 = AI_Player(self.ai_algo)
        player_2 = AI_Player(self.ai_algo)

        for _ in range(self.number_of_games):
            game = TicTacDoh(players=[player_1, player_2])
            score = game.play()
            self.scores.append(score)

if __name__ == "__main__":
    test = Test(3).start()