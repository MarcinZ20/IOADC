import gymnasium as gym
import cv2
from stable_baselines3 import A2C, SAC

env = gym.make("Humanoid-v4", render_mode="rgb_array")


# TODO - set parameters and check results - save in the file / curve
model = SAC('MlpPolicy', env,
            learning_rate=3e-10,
            # buffer_size=int(1e5),
            # batch_size=64,
            # gamma=0.99,
            # ent_coef='auto',
            # target_update_interval=1,
            # gradient_steps=64,
            learning_starts=10000,
            verbose=1)

model.learn(total_timesteps=10_000)

vec_env = model.get_env()
obs = vec_env.reset()
while True:
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    vec_env.render("human")
    # VecEnv resets automatically
    # if done:
    #   obs = vec_env.reset()