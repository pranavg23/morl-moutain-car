from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-speed",
    entry_point="mo_gymnasium.envs.mountain_car_speed.mountain_car_speed:MOMountainCar",
    max_episode_steps=200,
)
