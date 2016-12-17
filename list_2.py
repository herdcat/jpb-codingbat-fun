#Exercise1
count_evens = lambda nums: len([x for x in nums if x % 2 ==0])

#Exercise2
big_diff = lambda nums: max(nums) - min(nums)

#Exercise3
centered_average = lambda nums: sum(sorted(nums)[1:-1])/len(sorted(nums)[1:-1])

#Exercise4
sum13 = lambda nums: sum([x for i,x in enumerate(nums) if (nums[i-1]!=13 and nums[i]!=13 and i!=0) or ((nums[i]!=13) and i==0)])

#Exercise5
#Will come back to this

#Exercise6
has22 = lambda nums: "22" in "".join(["{0}".format(x) for x in nums])
