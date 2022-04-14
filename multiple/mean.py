import sys
import numpy as np

data_file = sys.argv[1]
out_file = sys.argv[-1]

data = np.loadtxt(data_file)
mean = np.mean(data)
np.savetxt(out_file, [mean])