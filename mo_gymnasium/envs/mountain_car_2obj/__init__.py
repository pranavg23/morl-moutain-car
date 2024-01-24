from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-2Obj",
    entry_point="mo_gymnasium.envs.mountain_car_2obj.mountain_car_2obj:MOMountainCar",
    max_episode_steps=200,
)
