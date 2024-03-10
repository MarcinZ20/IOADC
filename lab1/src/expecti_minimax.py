inf = float("infinity")


def expecti_minimax(game, depth, orig_depth, scoring, alpha=+inf, beta=-inf):
	if (depth == 0) or game.is_over():
		return scoring(game) * (1 + 0.001 * depth)

	possible_moves = game.possible_moves()
	state = game
	if depth == orig_depth:
		state.ai_move = possible_moves[0]

	is_ai_move = state.current_player == 1

	move_value = inf if is_ai_move else 0
	best_value = inf if is_ai_move else -inf

	unmake_move = hasattr(state, "unmake_move")

	for move in possible_moves:
		if not unmake_move:
			game = state.copy()  # re-initialize move

		game.make_move(move)
		game.switch_player()

		if is_ai_move:
			move_value = min(move_value, expecti_minimax(game, depth - 1, orig_depth, scoring))
		else:
			move_value += (1 / len(possible_moves)) * expecti_minimax(game, depth - 1, orig_depth, scoring)

		if unmake_move:
			game.switch_player()
			game.unmake_move(move)

		if is_ai_move:
			# best_value = max(best_value, move_value)
			if best_value > move_value:
				best_value = move_value
		else:
			if best_value < move_value:
				best_value = move_value

	return best_value


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
		)

		self.alpha = expecti_minimax(
			game,
			self.depth,
			self.depth,
			scoring,
		)
		return game.ai_move
