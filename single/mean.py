import numpy as np

data = np.loadtxt("data.txt")
mean = np.mean(data)
np.savetxt("mean.txt", [mean])