def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return sorted_arr(left,right,arr)


def sorted_arr(left,right,arr):
    i=j=k=0
    ll=len(left)
    rl=len(right)
    while i<ll and j<rl:
        if  left[i] < right[j]:
            arr[k]=left[i]
            k=k+1
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
            k = k + 1

    while i<ll:
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j<rl:
        arr[k] = right[j]
        j = j + 1
        k = k + 1


    return arr
arr=[200,300,10,2,4,7,5,1,67,87,55,5646,34525,5645,36235]
print(merge_sort(arr))