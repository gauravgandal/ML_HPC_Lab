import random
import time
from datetime import datetime
from multiprocessing import Pool

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_parallel(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i % 2, n-1, 2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    a = [random.randint(0, 10000) for _ in range(10000)]
    print("Unsorted Array:")
    print(a)

    # Serial sorting
    start = datetime.now()
    bubble_sort(a)
    end = datetime.now()
    duration = end - start
    print("Serial Sorted Array:")
    print(a)
    print("Serial Duration:", duration)

    a = [random.randint(0, 10000) for _ in range(10000)]

    # Parallel sorting
    print("\nParallel Sorting...")

    start = datetime.now()
    pool = Pool()
    result = pool.apply_async(bubble_sort_parallel, (a,))
    a = result.get()
    pool.close()
    pool.join()
    end = datetime.now()
    duration = end - start
    print("Parallel Sorted Array:")
    print(a)
    print("Parallel Duration:", duration)

if __name__ == "__main__":
    main()
