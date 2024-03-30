from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-speed-move",
    entry_point="mo_gymnasium.envs.mountain_car_move_speed_move.mountain_car_speed_move:MOMountainCar",
    max_episode_steps=200,
)
