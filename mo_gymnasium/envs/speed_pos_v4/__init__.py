from gymnasium.envs.registration import register


register(
    id="speed-pos",
    entry_point="mo_gymnasium.envs.speed_pos_v4.speed_pos_v4:MOMountainCar",
    max_episode_steps=200,
)
