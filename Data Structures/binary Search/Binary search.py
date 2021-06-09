def binaryseacrh(array,element):
    left=0
    right=len(array)-1
    mid=left+right//2
    i=0
    while left<=right:
        i=i+1
        if element==array[mid]:
            print("index:",mid)
            break

        if element > array[mid]:
            left=mid+1

        else:
            right=mid-1
        mid=(left+right)//2

li=[1,5,7,8,10,13,45,67,89,99,101,123,145,167,189,199]

binaryseacrh(li,123)


