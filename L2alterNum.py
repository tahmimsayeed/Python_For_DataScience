#1 2 3 4 5 6 7 8 9 10/ 1 3 5 7 9/ 1 5 9 / 1 9/ 1
n = 1000
nums = list(range(1, n + 1))
while len(nums) > 1:
    keep = []
    for i in range(len(nums)):
        if i % 2 == 0:
            keep.append(nums[i])
    if len(keep) == 1:           
        last_removed = nums[1]   
        nums = keep
print("Survivor:", nums[0])          
print("Last removed:", last_removed) 

people_list = []
