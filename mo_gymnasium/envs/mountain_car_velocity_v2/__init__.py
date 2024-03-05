from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-velocity-v2",
    entry_point="mo_gymnasium.envs.mountain_car_velocity_v2.mountain_car_velocity_v2:MOMountainCar",
    max_episode_steps=200,
)
