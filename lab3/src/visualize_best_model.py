import torch
import gymnasium as gym
from main import REINFORCE, Policy_Network

path = 'best_model.pt'

env = gym.make("InvertedPendulum-v5", render_mode="human")
wrapped_env = gym.wrappers.RecordEpisodeStatistics(env, 50)
obs_space_dims = env.observation_space.shape[0]
action_space_dims = env.action_space.shape[0]

net_loaded = Policy_Network(obs_space_dims, action_space_dims)
net_loaded.load_state_dict(torch.load(path))
agent = REINFORCE(obs_space_dims, action_space_dims, net_loaded)

observation, info = env.reset()

while True:
    action = agent.sample_action(observation)
    observation, reward, terminated, truncated, info = wrapped_env.step(action)

    if terminated:# or truncated:
        break
        # observation, info = env.reset()

env.close()