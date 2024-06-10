import torch
import torch.nn as nn
import torch.optim as optim
import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from pettingzoo.sisl import multiwalker_v9

# Custom wrapper to convert PettingZoo environment to Gym format
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize, VecFrameStack
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.ppo import MlpPolicy

class PettingZooEnvToGym:
    def __init__(self, pettingzoo_env):
        self.pettingzoo_env = pettingzoo_env
        original_action_space = pettingzoo_env.action_space('walker_0')
        self.action_space = gym.spaces.Box(low=original_action_space.low, high=original_action_space.high, shape=original_action_space.shape, dtype=original_action_space.dtype)
        
        # Assuming the observation space shape is (31,)
        low = np.full((31,), -np.finfo(np.float32).max)  # Large negative value
        high = np.full((31,), np.finfo(np.float32).max)  # Large positive value
        self.observation_space = gym.spaces.Box(low=low, high=high, dtype=np.float32)
        
        self.num_agents = None
        self.metadata = getattr(pettingzoo_env, 'metadata', {'render.modes': []})

    def reset(self):
        self.pettingzoo_env.reset()
        self.num_agents = len(self.pettingzoo_env.agents)
        return self.pettingzoo_env.observe('walker_0')

    def step(self, action):
        # Check if action is None or not an array/list, handle accordingly
        if action is None:
            raise ValueError("Action cannot be None")
        
        # Ensure action is in a format that can be evaluated by np.isnan
        try:
            # If action is already a NumPy array, this will pass through
            # If it's a list or similar, it will be converted to a NumPy array
            action_array = np.asarray(action, dtype=np.float32)
        except Exception as e:
            raise TypeError(f"Failed to convert action to a format compatible with np.isnan: {e}")
        
        # Check for NaN values in the action array
        if np.isnan(action_array).any():
            raise ValueError("Action array cannot contain NaN values")
        
        # Assuming actions need to be a dictionary mapping each agent to its action
        # This part might need adjustment based on the specific requirements of your environment
        actions = {agent: action_array for agent in self.pettingzoo_env.agents}
        
        # Proceed with the environment step
        observations, rewards, dones, infos = self.pettingzoo_env.step(actions)
        return observations, rewards, dones, infos
        

# Initialize the environment
pettingzoo_env = multiwalker_v9.env()
env = DummyVecEnv([lambda: PettingZooEnvToGym(pettingzoo_env)])

# Define and train the PPO model
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)

# Save the model
model.save("ppo_multiwalker")

# Plotting the learning curve
import matplotlib.pyplot as plt

# Retrieve training rewards
# Assuming the model contains a method to access episode rewards; if not, modify accordingly.
episode_rewards = model.episode_rewards

# Plot learning curve
plt.plot(episode_rewards)
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.title('Learning Curve')
plt.savefig('learning_curve.png')
plt.show()
