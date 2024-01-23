import random
import timeit

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Function for creating random arrays
def create_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


def main():
    # Array sizes for testing
    sizes = [100, 1000, 10000]

    # Measurements of execution time for each algorithm on different array sizes
    results = {"Insertion Sort": [], "Merge Sort": [], "Timsort (sorted)": []}

    for size in sizes:
        # Creating an array for testing
        array = create_random_array(size)

        # Time measurement for Insertion Sort
        results["Insertion Sort"].append(timeit.timeit(
            lambda: insertion_sort(array.copy()), number=1))

        # Time measurement for Merge Sort
        results["Merge Sort"].append(timeit.timeit(
            lambda: merge_sort(array.copy()), number=1))

        # Time measurement for Timsort
        results["Timsort (sorted)"].append(
            timeit.timeit(lambda: sorted(array), number=1))

    print(f"Array sizes for testing: {sizes}\n")
    print(f"Insertion Sort: {results["Insertion Sort"]}")
    print(f"Merge Sort: {results["Merge Sort"]}")
    print(f"Timsort (sorted): {results["Timsort (sorted)"]}")


if __name__ == "__main__":
    print(f"Homework 4 - Task 1 | Starting...\n")
    main()
    print(f"\nHomework 4 - Task 1 | Done")
