#Exercise1
count_evens = lambda nums: len([x for x in nums if x % 2 ==0])

#Exercise2
big_diff = lambda nums: max(nums) - min(nums)

#Exercise3
centered_average = lambda nums: sum(sorted(nums)[1:-1])/len(sorted(nums)[1:-1])

#Exercise4
#Will come back to this

#Exercise5
#Will come back to this

#Exercise6
has22 = lambda nums: "22" in "".join(["{0}".format(x) for x in nums])
