import os
from pathlib import Path

import supersuit as ss
from pettingzoo.atari import pong_v3

env = pong_v3.env(num_players=2, max_cycles=1000, render_mode='human', auto_rom_install_path=Path("~/.virtualenvs/ioadc/lib/python3.10/site-packages/AutoROM/roms/pong.bin"))
env = ss.max_observation_v0(env, 2)
env = ss.sticky_actions_v0(env, repeat_action_probability=0.25)
env = ss.frame_skip_v0(env, 4)
env = ss.frame_stack_v1(env, 4)
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        # this is where you would insert your policy
        action = env.action_space(agent).sample()

    env.step(action)

env.close()

