from gymnasium.envs.registration import register


register(
    id="velocity-pos",
    entry_point="mo_gymnasium.envs.velocity_pos_v4.velocity_pos_v4:MOMountainCar",
    max_episode_steps=200,
)
