inf = float("infinity")
def expecti_minimax(game, depth, origDepth, scoring, alpha=+inf, beta=-inf):
	return 0


class ExpectiMinimax:
	def __init__(self, depth, scoring=None, win_score=+inf):
		self.scoring = scoring
		self.depth = depth
		self.win_score = win_score

	def __call__(self, game):
		"""
		Returns the AI's best move given the current state of the game.
		"""

		scoring = (
			self.scoring if self.scoring else (lambda g: g.scoring())
		)  # horrible hack

		self.alpha = expecti_minimax(
			game,
			self.depth,
			self.depth,
			scoring,
			-self.win_score,
			+self.win_score,
		)
		return game.ai_move
