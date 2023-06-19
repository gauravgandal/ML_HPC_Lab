import random
import numpy as np
import time

N = 10000000

# Addition of two vectors
a = [random.randint(0, N) for _ in range(N)]
b = [random.randint(0, N) for _ in range(N)]
c = np.zeros(N, dtype=int)

start = time.time()
for i in range(N):
    c[i] = b[i] + a[i]
duration = time.time() - start
print("Serial vector addition:", duration)

start = time.time()
c_parallel = np.add(a, b)
duration = time.time() - start
print("Parallel vector addition:", duration)

# Print addition results
print("Addition results:")
print("Serial:   ", c)
print("Parallel: ", c_parallel)

print("***********************************")
