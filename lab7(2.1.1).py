nums = [11,4,7,5,10,9,13,1]
def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False
    while not sorted:
        sorted = True
        for x in range(0,indexing_length):
            if list_a[x] > list_a[x+1]:
                sorted = False
                list_a[x],list_a[x+1] = list_a[x+1],list_a[x]
    return list_a
print(nums)
