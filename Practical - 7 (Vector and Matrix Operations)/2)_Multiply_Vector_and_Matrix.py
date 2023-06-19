import random
import numpy as np
import time

M = 700

# Multiply Vector and matrix
A = np.random.randint(0, M, size=(M, M))
a = np.random.randint(0, M, size=M)
d = np.zeros(M, dtype=int)

# Serial multiplication
start = time.time()
for i in range(M):
    sum = 0
    for j in range(M):
        sum += A[i][j] * a[j]
    d[i] = sum
serial_duration = time.time() - start
print("Serial Multiply Vector and matrix:", serial_duration)

# Parallel multiplication
start = time.time()
d_parallel = np.dot(A, a)
parallel_duration = time.time() - start
print("Parallel Multiply Vector and matrix:", parallel_duration)

# Print multiplication results
print("Multiplication results:")
print("Serial:   ", d)
print("Parallel: ", d_parallel)

print("***********************************")
