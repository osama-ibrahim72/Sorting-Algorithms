def selectionSort (arr,size):
    for i in range(0,size,1):
        least = 1
        #select smallest element
        for j in range(i+1,size,1):
            if arr[j]<arr[least]:
                least = j
        #swap elements
        arr[i],arr[least] = arr[least],arr[i]