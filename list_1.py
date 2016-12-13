#Exercise1
first_last6 = lambda nums: (nums[0]==6) or (nums[-1]==6)

#Exercise2
same_first_last = lambda nums: nums[0]==nums[-1] if len(nums)>0 else False

#Exercise3
make_pi = lambda: [3,1,4]

#Exercise4
common_end = lambda a, b: (a[0]==b[0]) or (a[-1]==b[-1])

#Exercise5
sum3 = lambda nums: sum(nums)

#Exercise6
rotate_left3 = lambda nums: [nums[1],nums[2],nums[0]]

#Exercise7
reverse3 = lambda nums: nums[::-1]

#Exercise8
max_end3 = lambda nums: [nums[0]]*3 if nums[0]>=nums[-1] else [nums[-1]]*3

#Exercise9
#I'll come back to this one

#Exercise10
middle_way = lambda a, b: [a[1],b[1]]

#Exercise11
make_ends = lambda nums: [nums[0],nums[-1]]

#Exercise12
has23 = lambda nums: 2 in nums or 3 in nums
