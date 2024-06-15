def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True  # Key found
        elif arr[mid] < key:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return False  # Key not found

def linear_search(arr, key):
    for element in arr:
        if element == key:
            return True  # Key found

    return False  # Key not found

# Example usage
arr = [10, 12, 39, 49, 51, 65, 68, 74]

# Searching for 10
key = 10
binary_search_result_10 = binary_search(arr, key)
linear_search_result_10 = linear_search(arr, key)
print("10 using binary search:", binary_search_result_10)
print("10 using linear search:", linear_search_result_10)

# Searching for 65
key = 65
binary_search_result_65 = binary_search(arr, key)
linear_search_result_65 = linear_search(arr, key)
print("65 using binary search:", binary_search_result_65)
print("65 using linear search:", linear_search_result_65)

# Comparison of search methods
if binary_search_result_10:
    print("Binary search is faster to find 10")
else:
    print("Linear search is faster to find 10")

if binary_search_result_65:
    print("Binary search is faster to find 65")
else:
    print("Linear search is faster to find 65")
