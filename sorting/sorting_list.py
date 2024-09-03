import random
import timeit

# Step 1: Generate a random list of numbers from 1 to 100
def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

# Step 2: Sorting function using Bubble Sort (without using sort function)
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Step 3: Function to time the sorting process
def measure_sorting_time():
    # Generate a random list of size 20 for demonstration
    random_list = generate_random_list(20)
    print("Original List:", random_list)

    # Measure the time taken to sort the list
    start_time = timeit.default_timer()
    sorted_list = bubble_sort(random_list)
    end_time = timeit.default_timer()

    # Print the sorted list and the time taken
    print("Sorted List:", sorted_list)
    print(f"Time taken to sort: {end_time - start_time} seconds")

# Run the function to measure sorting time
measure_sorting_time()
