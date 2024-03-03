from gymnasium.envs.registration import register


register(
    id="mountaincar3obj",
    entry_point="mo_gymnasium.envs.mountaincar3obj.mountaincar3obj:MOMountainCar",
    max_episode_steps=200,
)
