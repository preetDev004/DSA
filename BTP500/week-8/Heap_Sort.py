def heapify(arr,n , i):
    largest = i
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # Find largest among root and children
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursive call
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i ,0)

if __name__ == "__main__":
    arr = [12, 30, 11, 13, 23, 5, 6, 7]
    heap_sort(arr)
    print(arr)