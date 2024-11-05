import random
import time

def deterministic_quick_sort(arr):
    """Deterministic Quick Sort using the last element as pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    """Randomized Quick Sort."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Move pivot to the end
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]
    
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

def analyze_sort(sort_function, arr):
    """Analyze the sorting function performance."""
    start_time = time.time()
    sorted_array = sort_function(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_array, execution_time

def get_user_input():
    """Get an array input from the user."""
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    return arr

if __name__ == "__main__":
    # Get input from the user
    array = get_user_input()

    # Analyze Deterministic Quick Sort
    det_sorted, det_time = analyze_sort(deterministic_quick_sort, array.copy())
    print(f"\nDeterministic Quick Sort Time: {det_time:.6f} seconds")
    print("Sorted Array (Deterministic):", det_sorted)

    # Analyze Randomized Quick Sort
    rand_sorted, rand_time = analyze_sort(randomized_quick_sort, array.copy())
    print(f"\nRandomized Quick Sort Time: {rand_time:.6f} seconds")
    print("Sorted Array (Randomized):", rand_sorted)
