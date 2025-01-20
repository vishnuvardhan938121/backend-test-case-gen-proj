import random

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    for i in range(n):
        arr[i] = output[i]

# Function to generate test cases
def generate_test_cases(algo_type, algo_name):
    test_cases = []

    for _ in range(20):  # Generate 20 test cases
        arr_length = random.randint(5, 10)
        arr = random.sample(range(1, 100), arr_length)
        
        test_case = {
            "input": arr,
        }

        # Generate test case for sorting algorithms
        if algo_type == "sorting":
            if algo_name == "bubble_sort":
                test_case["expected_output"] = bubble_sort(arr.copy())
            elif algo_name == "selection_sort":
                test_case["expected_output"] = selection_sort(arr.copy())
            elif algo_name == "insertion_sort":
                test_case["expected_output"] = insertion_sort(arr.copy())
            elif algo_name == "merge_sort":
                test_case["expected_output"] = merge_sort(arr.copy())
            elif algo_name == "quick_sort":
                test_case["expected_output"] = quick_sort(arr.copy())
            elif algo_name == "heap_sort":
                test_case["expected_output"] = heap_sort(arr.copy())
            elif algo_name == "counting_sort":
                test_case["expected_output"] = counting_sort(arr.copy())
            elif algo_name == "radix_sort":
                test_case["expected_output"] = radix_sort(arr.copy())

        test_cases.append(test_case)

    return test_cases


# Example usage:
test_cases = generate_test_cases("sorting", "bubble_sort")
for case in test_cases:
    print(f"Input: {case['input']}, Expected Output: {case['expected_output']}")
