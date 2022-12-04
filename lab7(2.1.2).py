nums = [11,4,7,5,10,9,13,1]
def selection_sort(nums):
    for x in range (0,len(nums) -1):
        cur_min_idx = x
        for i in range(i+1,len(num)):
            if nums[i] < nums[cur_min_idx]:
                cur_min_idx = i
        nums[x],nums[cur_min_idx] = nums[cur_min_idx],nums[x]

print(nums)
