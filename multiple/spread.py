import sys
import numpy as np

data_file = sys.argv[1]
out_file = sys.argv[2]

data = np.loadtxt(data_file)
spread = np.std(data)
# spread = 0.5 * (np.percentile(data, 84) - np.percentile(data, 16))
np.savetxt(out_file, [spread])