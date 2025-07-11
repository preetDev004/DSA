sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# implementation of linear search
#  Time Complexity -> O(n), Space Complexity -> O(1)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i]
    return -1

# implementation of binary search
#  Time Complexity -> O(log n), Space Complexity -> O(1)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right and result == -1:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = arr[mid]
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result


unsorted_list = [5, 3, 6, 2, 10, 23, 1, 323, 121, 32, 12, 23, 43, 2, 54]

# implementation of quick sort
#  Time Complexity Average Case -> Θ(n log n), Space Complexity -> O(log n)
#  Time Complexity Worst Case -> O(n^2)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[(len(arr) - 1) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# implementation of merge sort
#  Time Complexity -> O(n log n), Space Complexity -> O(n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

if __name__ == "__main__":
    print(binary_search(sorted_list, 8))
    print(binary_search(sorted_list, 8))
    print(quick_sort(unsorted_list))
    print(merge_sort(unsorted_list))
