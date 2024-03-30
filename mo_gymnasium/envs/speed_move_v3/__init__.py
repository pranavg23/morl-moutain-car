from gymnasium.envs.registration import register


register(
    id="speed-move-v3",
    entry_point="mo_gymnasium.envs.speed_move_v3.speed_move_v3:MOMountainCar",
    max_episode_steps=200,
)
