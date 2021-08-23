def bubble_sort(arr):
    for i in range(len(arr),0,-1):
        for j in range(1,i):
            if arr[j-1]>arr[j]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp

    print(arr)

bubble_sort([100,20,45,333,46,67,43,356,2342,2342])