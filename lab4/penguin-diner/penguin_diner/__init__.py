from gymnasium.envs.registration import register

register(
     id="penguin_diner/PenguinWorld-v0",
     entry_point="penguin_diner.envs:PenguinWorld",
     max_episode_steps=300,
)