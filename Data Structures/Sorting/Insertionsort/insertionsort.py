def insertion_sort(data):
    for i in range(1,len(data)):
    
        value=data[i]
        j=i-1
        while j>=0 and value < data[j]:
            data[j+1]=data[j]
            j=j-1

        data[j+1]=value
    print(data)

insertion_sort([89,56,65,46,446,3534,34532,132,12,45,00,0,6])
