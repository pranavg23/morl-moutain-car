import math
from typing import Optional

import numpy as np
from gymnasium import spaces
from gymnasium.envs.classic_control.mountain_car import MountainCarEnv
from gymnasium.utils import EzPickle


class MOMountainCar(MountainCarEnv, EzPickle):
    """
    A multi-objective version of the MountainCar environment, where the goal is to reach the top of the mountain.

    See [Gymnasium's env](https://gymnasium.farama.org/environments/classic_control/mountain_car_continuous/) for more information.

    ## Reward space:
    The reward space is a 3D vector containing the time penalty, and penalties for reversing and going forward.
    - time penalty: -1.0 for each time step
    - reverse penalty: -1.0 for each time step the action is 0 (reverse)
    - forward penalty: -1.0 for each time step the action is 2 (forward)
    """

    def __init__(self, render_mode: Optional[str] = None, goal_velocity=0):
        super().__init__(render_mode, goal_velocity)
        EzPickle.__init__(self, render_mode, goal_velocity)

        self.reward_space = spaces.Box(low=np.array([-1, 0]), high=np.array([0, np.inf]), shape=(2,), dtype=np.float32)
        self.reward_dim = 2
        print(self.reward_space)

    def step(self, action: int):
        assert self.action_space.contains(action), f"{action!r} ({type(action)}) invalid"

        position, velocity = self.state
        velocity += (action - 1) * self.force + math.cos(3 * position) * (-self.gravity)
        velocity = np.clip(velocity, -self.max_speed, self.max_speed) #Do we need consider changing the clipping?
        position += velocity
        position = np.clip(position, self.min_position, self.max_position)
        if position == self.min_position and velocity < 0:
            velocity = 0

        terminated = bool(position >= self.goal_position and velocity >= self.goal_velocity)
        # reward = -1.0
        reward = np.zeros(2, dtype=np.float32)
        reward[0] = 0.0 if action == 1 else -1.0  # movement penalty
        reward[1] = 100*abs(velocity) #Rewarding magnitude of velocity

        self.state = (position, velocity)
        if self.render_mode == "human":
            self.render()
        return np.array(self.state, dtype=np.float32), reward, terminated, False, {}
