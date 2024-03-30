from gymnasium.envs.registration import register


register(
    id="speed-move-v2",
    entry_point="mo_gymnasium.envs.speed_move_v2.speed_move_v2:MOMountainCar",
    max_episode_steps=200,
)
