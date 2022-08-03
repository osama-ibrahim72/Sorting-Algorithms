def insertionSort(arr, size):
    for i in range(0, size, 1):
        tmp = arr[i]
        j = i
        #move all elements arr[j]>arr[i] one position
        while j > 0 and tmp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        #insert the element in correct position
        arr[j] = tmp
