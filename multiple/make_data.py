import numpy as np
np.random.seed(123)

n_data_files = 100

for i in range(n_data_files):
    data = np.random.normal(0, 1, 1000)
    np.savetxt(f"data/data_{i}.txt", data)
