# pip install -e penguin-diner
import penguin_diner
import gymnasium
import random
import time


env = gymnasium.make('penguin_diner/PenguinWorld-v0', render_mode='human')


state, _ = env.reset()
done = False
score = 0

while not done:
	action = random.randint(0, 3)

	state, reward, terminated, truncated, info = env.step(action)

	print(state)

	score += reward

	# done = terminated or truncated

	print(score)
	time.sleep(0.1)

env.close()

