def bubbleSort ( arr , size):
    for i in range(0,size,1):
        for j in range(size-1, i, -1):
            if(arr[j]<arr[j-1]):
                #swap values
                tmp = arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=tmp