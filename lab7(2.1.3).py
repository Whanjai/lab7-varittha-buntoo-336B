arr = [11,4,7,5,10,9,13,1]
def insertion_sort(arr):
    for i in range (1,ln(arr)):
        j = 1
        while arr[j-1] > arr[j] and j>0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1

print(arr)
