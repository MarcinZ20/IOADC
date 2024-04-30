# pip install -e penguin-diner
import penguin_diner
import gymnasium
import random
import numpy as np
from tqdm import tqdm
import time
from solution_qlearning import Qlearning, EpsilonGreedy


# env = gymnasium.make('penguin_diner/PenguinWorld-v0', render_mode='human')
env = gymnasium.make('penguin_diner/PenguinWorld-v0')

print(env.observation_space)
print(env.spec)

learner = Qlearning(
    learning_rate=0.1,
    gamma=0.95,
    state_size=128,
    action_size=4,
)
explorer = EpsilonGreedy(
    epsilon=0.01,
)
learner.reset_qtable()
states = []
n_runs = 1000
run = 0
episodes = range(n_runs)

print("Q table before learning:", learner.qtable)

for episode in tqdm(episodes, desc=f"Run {run}/{n_runs} - Episodes", leave=False):

	state, _ = env.reset()
	agent_has_object = state['agent_has_object']

	state = state['agent'][0] * 8 + state['agent'][1]
	state = state * 2 if agent_has_object else state

	score = 0
	step = 0
	done = False

	while not done:

		# action = random.randint(0, 3)

		action = explorer.choose_action(
			action_space=env.action_space, state=state, qtable=learner.qtable
		)

		new_state, reward, terminated, truncated, info = env.step(action)
		agent_has_object = new_state['agent_has_object']

		new_state = new_state['agent'][0] * 8 + new_state['agent'][1]
		new_state = new_state * 2 if agent_has_object else new_state
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

print("Q table after learning:", learner.qtable)

env2 = gymnasium.make('penguin_diner/PenguinWorld-v0', render_mode='human')
state, _ = env2.reset()
agent_has_object = state['agent_has_object']

state = state['agent'][0] * 8 + state['agent'][1]
state = state * 2 if agent_has_object else state
print("State:", state)
# state = state['agent'][0] * 5 + state['agent'][1]

done = False
score = 0
while not done:
	# action = random.randint(0, 3)

	action = explorer.choose_action(
		action_space=env2.action_space, state=state, qtable=learner.qtable
	)

	new_state, reward, terminated, truncated, info = env2.step(action)
	agent_has_object = new_state['agent_has_object']

	new_state = new_state['agent'][0] * 8 + new_state['agent'][1]
	new_state = new_state * 2 if agent_has_object else new_state
	states.append(new_state)
	score += reward

	learner.qtable[state, action] = learner.update(
		state, action, reward, new_state
	)

	# done = terminated or truncated

	# time.sleep(0.1)
	state = new_state

