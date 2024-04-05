import matplotlib.pyplot as plt
import numpy as np

# Read trajectory data
traj_data = np.loadtxt("traj")
timesteps = traj_data[:, 0]
positions = traj_data[:, 1]
velocities = traj_data[:, 2]
actions = traj_data[:, 3]

# Plot trajectory data
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(timesteps, positions, label="Position")
plt.xlabel("Timesteps")
plt.ylabel("Position")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(timesteps, velocities, label="Velocity", color="orange")
plt.xlabel("Timesteps")
plt.ylabel("Velocity")
plt.legend()

plt.tight_layout()
plt.show()

# Read duration data
dura_data = np.loadtxt("dura")
trials = dura_data[:, 0]
durations = dura_data[:, 1]

# Plot duration data
plt.figure(figsize=(8, 4))
plt.plot(trials, durations, marker='o', linestyle='-', color='b')
plt.xlabel("Trials")
plt.ylabel("Duration")
plt.title("Duration of Each Trial")
plt.show()
