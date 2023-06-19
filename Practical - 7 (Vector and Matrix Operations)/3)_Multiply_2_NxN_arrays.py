import random
import numpy as np
import time
from multiprocessing import Pool

N = 100

A = np.random.randint(0, N, size=(N, N))
B = np.random.randint(0, N, size=(N, N))
C = np.zeros((N, N), dtype=int)

def multiply_element(i, j):
    result = 0
    for k in range(N):
        result += A[i][k] * B[k][j]
    return result

# Serial matrix multiplication
start = time.time()
for i in range(N):
    for j in range(N):
        C[i][j] = 0
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]
serial_duration = time.time() - start
print("Serial Multiply Matrix and matrix:", serial_duration)

# Parallel matrix multiplication
start = time.time()
pool = Pool()  # Create a pool of worker processes
indices = [(i, j) for i in range(N) for j in range(N)]
results = pool.starmap(multiply_element, indices)  # Apply the function to each element in parallel
pool.close()
pool.join()

# Reshape the results into a matrix
C_parallel = np.array(results).reshape((N, N))
parallel_duration = time.time() - start
print("Parallel Multiply Matrix and matrix:", parallel_duration)

# Print multiplication results
print("Multiplication results:")
print("Serial:   ")
print(C)
print("Parallel: ")
print(C_parallel)

print("***********************************")
