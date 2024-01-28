from gymnasium.envs.registration import register


register(
    id="mo-mountaincar-enengy",
    entry_point="mo_gymnasium.envs.mountain_car_energy.mountain_car_energy:MOMountainCar",
    max_episode_steps=200,
)
