from gymnasium.envs.registration import register


register(
    id="mountaincar3obj",
    entry_point="mo_gymnasium.envs.mountain_car_3obj.mountain_car_3obj:MOMountainCar",
    max_episode_steps=200,
)
