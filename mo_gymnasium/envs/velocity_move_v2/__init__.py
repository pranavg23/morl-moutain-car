from gymnasium.envs.registration import register


register(
    id="velocity-move-v2",
    entry_point="mo_gymnasium.envs.velocity_move_v2.velocity_move_v2:MOMountainCar",
    max_episode_steps=200,
)
