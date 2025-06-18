import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("data.csv", delimiter=',', skip_header=1)

tail_x = data[:, 0]
tail_y = data[:, 1]
head_x = data[:, 2]
head_y = data[:, 3]

theta = np.arctan2(head_y - tail_y, head_x - tail_x)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].plot(head_x, head_y, 'r.', label='head')
axes[0].plot(tail_x, tail_y, 'b.', label='tail')
axes[0].set_title("Trajectory of the Robot")
axes[0].set_xlabel("x-loc (unit)")
axes[0].set_ylabel("y-loc (unit)")
axes[0].legend()

frames = np.arange(len(theta))
axes[1].plot(frames, theta, 'g^-')
axes[1].set_title("Orientation of the Robot")
axes[1].set_xlabel("frame #")
axes[1].set_ylabel("theta [rad]")

plt.tight_layout()
plt.show()
