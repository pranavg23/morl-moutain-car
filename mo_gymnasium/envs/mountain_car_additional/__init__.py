from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-additional",
    entry_point="mo_gymnasium.envs.mountain_car_additional.mountain_car_additional:MOMountainCar",
    max_episode_steps=200,
)
