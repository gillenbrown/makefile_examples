import sys
import numpy as np
import matplotlib.pyplot as plt

mean_files = []
spread_files = []
for f in sys.argv[1:]:
    if "mean_" in f:
        mean_files.append(f)
    elif "spread_" in f:
        spread_files.append(f)

fig, ax = plt.subplots()
y = 0
for mean_file, spread_file in zip(mean_files, spread_files):
    mean = np.loadtxt(mean_file)
    spread = np.loadtxt(spread_file)

    ax.errorbar(mean, y, xerr=spread, fmt=".", c="k")

    y += 1

ax.set_xlabel("Value")
ax.set_ylabel("Data File Number")
fig.savefig("plot.pdf")