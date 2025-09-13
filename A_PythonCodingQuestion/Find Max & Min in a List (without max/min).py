nums = [15, 2, 39, 8, 23, 1]


max_num=nums[0]
min_num=nums[1]


for n in nums:
    if n>max_num:
        max_num=n
    if n<min_num:
        min_num=n

print(max_num,min_num)