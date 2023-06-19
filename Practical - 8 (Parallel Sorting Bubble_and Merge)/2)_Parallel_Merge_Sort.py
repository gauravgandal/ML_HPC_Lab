import concurrent.futures
import time

def merge(a, i1, j1, i2, j2):
    temp = []
    i, j = i1, i2
    while i <= j1 and j <= j2:
        temp.append(a[i] if a[i] < a[j] else a[j])
        i, j = (i + 1, j) if a[i] < a[j] else (i, j + 1)
    temp.extend(a[i: j1 + 1])
    temp.extend(a[j: j2 + 1])
    a[i1: j2 + 1] = temp

def mergesort(a, i, j):
    if i < j:
        mid = (i + j) // 2
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(mergesort, a, i, mid)
            future2 = executor.submit(mergesort, a, mid + 1, j)
            future1.result()
            future2.result()
        merge(a, i, mid, mid + 1, j)

if __name__ == "__main__":
    a = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 1, 50, 48]

    print("Unsorted array:")
    for element in a:
        print(element)

    # Serial sorting
    a_serial = a.copy()
    start_serial = time.time()
    mergesort(a_serial, 0, len(a_serial) - 1)
    end_serial = time.time()
    print("\nSerial Sorted array:")
    for element in a_serial:
        print(element)
    print("Serial Execution time:", end_serial - start_serial, "seconds")

    # Parallel sorting
    a_parallel = a.copy()
    start_parallel = time.time()
    mergesort(a_parallel, 0, len(a_parallel) - 1)
    end_parallel = time.time()
    print("\nParallel Sorted array:")
    for element in a_parallel:
        print(element)
    print("Parallel Execution time:", end_parallel - start_parallel, "seconds")
