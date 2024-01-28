from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-velocity-move",
    entry_point="mo_gymnasium.envs.mountain_car_move_velocity_move.mountain_car_velocity_move:MOMountainCar",
    max_episode_steps=200,
)
