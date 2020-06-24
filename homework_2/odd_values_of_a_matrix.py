import numpy as np


arr = np.array([[np.random.randint(1, 10) for _ in range(10)] for _ in range(50)])
for i in arr.flat:
    if i % 2 == 1:
        print(i, end=", ")