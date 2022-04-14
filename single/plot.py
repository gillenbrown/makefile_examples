import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
mean = np.loadtxt("mean.txt")
spread = np.loadtxt("spread.txt")

fig, ax = plt.subplots()
ax.hist(data, bins=np.arange(-5, 5.01, 0.5))
ax.axvline(mean, ls=":", color="k", zorder=10)
ax.plot([-spread, spread], [0, 0], lw=10, zorder=10)
ax.set_xlabel("Value")
ax.set_ylabel("Number")
ax.set_xlim(-5, 5)
fig.savefig("plot.pdf")