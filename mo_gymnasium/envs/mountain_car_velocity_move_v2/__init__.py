from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-velocity-move-v2",
    entry_point="mo_gymnasium.envs.mountain_car_move_velocity_move_v2.mountain_car_velocity_move:MOMountainCar",
    max_episode_steps=200,
)
