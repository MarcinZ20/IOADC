# pip install -e penguin-diner
import penguin_diner
import gymnasium
import random
import numpy as np
from tqdm import tqdm
import time
from solution import Qlearning, EpsilonGreedy


# env = gymnasium.make('penguin_diner/PenguinWorld-v0', render_mode='human')
env = gymnasium.make('penguin_diner/PenguinWorld-v0')
print("Spec:", env.observation_space)

state, _ = env.reset()
state = state['agent'][0] * 5 + state['agent'][1]
done = False
score = 0

learner = Qlearning(
    learning_rate=0.1,
    gamma=0.95,
    state_size=25,
    action_size=4,
)
explorer = EpsilonGreedy(
    epsilon=0.1,
)
learner.reset_qtable()
states = []
n_runs = 100
run = 0
episodes = np.arange(n_runs)
for episode in tqdm(episodes, desc=f"Run {run}/{n_runs} - Episodes", leave=False):
	while not done:

		# action = random.randint(0, 3)

		action = explorer.choose_action(
			action_space=env.action_space, state=state, qtable=learner.qtable
		)

		new_state, reward, terminated, truncated, info = env.step(action)
		new_state = new_state['agent'][0] * 5 + new_state['agent'][1]
		states.append(new_state)
		score += reward

		learner.qtable[state, action] = learner.update(
			state, action, reward, new_state
		)

		done = terminated or truncated

		# time.sleep(0.1)
		state = new_state
	run += 1
# env.close()

