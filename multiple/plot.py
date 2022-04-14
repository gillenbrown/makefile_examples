import sys
import numpy as np
import matplotlib.pyplot as plt

data_files = sys.argv[1:]


fig, ax = plt.subplots()
for y, df in enumerate(data_files):
    mean_file = df.replace("data_", "mean_")
    spread_file = df.replace("data_", "spread_")

    mean = np.loadtxt(mean_file)
    spread = np.loadtxt(spread_file)

    ax.errorbar(mean, y, xerr=spread, fmt=".", c="k")

ax.set_xlabel("Value")
ax.set_ylabel("Data File Number")
fig.savefig("plot.pdf")