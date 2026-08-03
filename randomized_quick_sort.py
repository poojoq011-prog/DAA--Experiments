"""
Experiment No. 10
Improving Quick Sort Efficiency using Randomized Algorithm

Aim:
Implement and compare Deterministic Quick Sort and Randomized Quick Sort
by measuring execution time and number of comparisons for different
input configurations.
"""

import random
import time

# Global counters
det_comparisons = 0
rand_comparisons = 0


# ------------------ Deterministic Quick Sort ------------------

def det_partition(arr, low, high):
    global det_comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        det_comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot = det_partition(arr, low, high)

        deterministic_quick_sort(arr, low, pivot - 1)
        deterministic_quick_sort(arr, pivot + 1, high)


# ------------------ Randomized Quick Sort ------------------

def rand_partition(arr, low, high):
    global rand_comparisons

    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        rand_comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = rand_partition(arr, low, high)

        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)


# ------------------ Performance Test ------------------

def compare_algorithms(name, data):
    global det_comparisons, rand_comparisons

    print("\n" + "=" * 60)
    print(f"Input Type : {name}")
    print("=" * 60)

    # Deterministic Quick Sort
    det_data = data.copy()
    det_comparisons = 0

    start = time.perf_counter()
    deterministic_quick_sort(det_data, 0, len(det_data) - 1)
    det_time = time.perf_counter() - start

    # Randomized Quick Sort
    rand_data = data.copy()
    rand_comparisons = 0

    start = time.perf_counter()
    randomized_quick_sort(rand_data, 0, len(rand_data) - 1)
    rand_time = time.perf_counter() - start

    print("Deterministic Quick Sort")
    print(f"Execution Time : {det_time:.6f} seconds")
    print(f"Comparisons    : {det_comparisons}")

    print()

    print("Randomized Quick Sort")
    print(f"Execution Time : {rand_time:.6f} seconds")
    print(f"Comparisons    : {rand_comparisons}")


# ------------------ Main Program ------------------

def main():
    SIZE = 1000

    random_array = random.sample(range(1, 10001), SIZE)

    sorted_array = sorted(random_array)

    reverse_sorted_array = sorted(random_array, reverse=True)

    nearly_sorted_array = sorted_array.copy()
    for _ in range(20):
        i = random.randint(0, SIZE - 1)
        j = random.randint(0, SIZE - 1)
        nearly_sorted_array[i], nearly_sorted_array[j] = (
            nearly_sorted_array[j],
            nearly_sorted_array[i],
        )

    compare_algorithms("Random", random_array)
    compare_algorithms("Sorted", sorted_array)
    compare_algorithms("Reverse Sorted", reverse_sorted_array)
    compare_algorithms("Nearly Sorted", nearly_sorted_array)


if __name__ == "__main__":
    main()

OUTPUT:

Input Type DQS Comps DQS Time(ms) RQS Comps RQS Time(ms)
------------------------------------------------------------------------
Random 55821 1.82 56243 1.79
Sorted 12497500 312.45 60312 1.91
Reverse 12497500 318.22 58741 1.88
Nearly Sorted 6248000 156.23 57892 1.85
