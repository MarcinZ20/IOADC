import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import supersuit as ss

from pettingzoo.atari import pong_v3
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback

# Path to the AutoROM directory
env_path = Path('/Users/marcin/.pyenv/versions/3.10.13/lib/python3.10/site-packages/AutoROM/roms')


env = pong_v3.env(num_players=2, max_cycles=1000, render_mode='human', auto_rom_install_path=Path(env_path))
env = ss.max_observation_v0(env, 2)
env = ss.sticky_actions_v0(env, repeat_action_probability=0.25)
env = ss.frame_skip_v0(env, 4)
env = ss.frame_stack_v1(env, 4)
env.reset(seed=42)

class RewardCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(RewardCallback, self).__init__(verbose)
        self.episode_rewards = []

    def _on_step(self) -> bool:
        self.episode_rewards.append(self.locals["rewards"])
        return True
    
# Create the callback: check every 1000 steps
callback = RewardCallback()

model = PPO("CnnPolicy", env, verbose=1)
model.learn(total_timesteps=100000, callback=callback)

# Plotting the rewards
mean_rewards = [np.mean(callback.episode_rewards[i:i + 100]) for i in range(0, len(callback.episode_rewards), 100)]
plt.plot(mean_rewards)
plt.xlabel('Episodes (x100)')
plt.ylabel('Mean Total Reward')
plt.title('Learning Curve')
plt.show()

# for agent in env.agent_iter():
#     observation, reward, termination, truncation, info = env.last()

#     if termination or truncation:
#         action = None
#     else:
#         # this is where you would insert your policy
#         action = env.action_space(agent).sample()

#     env.step(action)

env.close()

