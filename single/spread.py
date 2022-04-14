import numpy as np

data = np.loadtxt("data.txt")
spread = np.std(data)
# spread = 0.5 * (np.percentile(data, 84) - np.percentile(data, 16))
np.savetxt("spread.txt", [spread])