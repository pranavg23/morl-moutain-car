from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-velocity",
    entry_point="mo_gymnasium.envs.mountain_car_velocity.mountain_car_velocity:MOMountainCar",
    max_episode_steps=200,
)
