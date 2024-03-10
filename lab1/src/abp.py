from math import inf
from easyAI import TwoPlayerGame
from typing import Any
from random import choice

class Node():

    def __init__(self) -> None:
       pass

class Minimax():
    def __init__(self, depth: int = 6) -> None:
        self.depth = depth
        self.alpha = -inf
        self.beta = inf

    def minimax(self, game: TwoPlayerGame, depth: int = 3, isMaximizingPlayer: bool = True) -> int:
        if depth == 0 or game.is_over():
            return 0

        if isMaximizingPlayer:
            max_eval = -inf
            for move in game.possible_moves():
                game_copy = game.copy()
                game_copy.make_move(move)
                eval = self.minimax(game_copy, depth - 1, False)
                max_eval = max(max_eval, eval)
                self.alpha = max(self.alpha, eval)
                if self.beta <= self.alpha:
                    break  # Beta cut-off
            return max_eval
        else:
            min_eval = inf
            for move in game.possible_moves():
                game_copy = game.copy()
                game_copy.make_move(move)
                eval = self.minimax(game_copy, depth - 1, True)
                min_eval = min(min_eval, eval)
                self.beta = min(self.beta, eval)
                if self.beta <= self.alpha:
                    break  # Alpha cut-off
            return min_eval

    def __call__(self, game: TwoPlayerGame) -> Any:
        best_score = -inf
        best_move = None

        for move in game.possible_moves():
            game_copy = game.copy()
            game_copy.make_move(move)
            score = self.minimax(game_copy, self.depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move if best_move is not None else choice(game.possible_moves())

        

