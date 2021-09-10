
def swap(a,b):
    return b,a

def quick_sort(arr,start,end):
    pivot=end
    pi=start
    for i in range(end):
        if arr[i]<=arr[pivot]:
            arr[i],arr[pi]=swap(arr[i],arr[pi])
            pi =pi+1

    arr[pivot], arr[pi] = swap(arr[pivot], arr[pi])
    if len(arr[:pi])>1:
     arr[:pi]=quick_sort(arr[:pi],0,len(arr[:pi])-1)
    if len(arr[pi+1:])>1:
        arr[pi+1:] = quick_sort(arr[pi+1:], 0, len(arr[pi+1:]) - 1)


    return arr

arr=[[5,10,3,2,1,7,6,4],[1,0],[100,203,834,5646,2342]]
for i in arr:
    print(quick_sort(i,0,len(i)-1))