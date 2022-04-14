import numpy as np
np.random.seed(123)

data = np.random.normal(0, 1, 1000)
np.savetxt("data.txt", data)