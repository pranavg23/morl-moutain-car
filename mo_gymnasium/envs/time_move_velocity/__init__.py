from gymnasium.envs.registration import register


register(
    id="time_move_velocity",
    entry_point="mo_gymnasium.envs.time_move_velocity.time_move_velocity:MOMountainCar",
    max_episode_steps=200,
)
