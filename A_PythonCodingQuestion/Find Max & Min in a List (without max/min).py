nums = [15, 2, 39, 8, 23, 1]


max_num=nums[0]
min_num=nums[1]


for n in nums:
    if n>max_num:
        max_num=n
    if n<min_num:
        min_num=n

print(max_num,min_num)

















lis=[11,3,66,86,97]

max_lis=lis[0]
min_lis=lis[1]


for n in lis:
    if n>max_lis:
        max_lis=n
    if n<min_lis:
        min_lis=n

print(max_lis,min_lis)