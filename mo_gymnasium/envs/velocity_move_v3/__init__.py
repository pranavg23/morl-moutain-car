from gymnasium.envs.registration import register


register(
    id="velocity-move-v3",
    entry_point="mo_gymnasium.envs.velocity_move_v3.velocity_move_v3:MOMountainCar",
    max_episode_steps=200,
)
