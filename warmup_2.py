#Exercise1
string_times = lambda str, n: str*n

#Exercise2
front_times = lambda str, n: str*n if len(str)<=3 else str[0:3]*n

#Exercise3
string_bits = lambda str: "".join([x for i, x in enumerate(str) if i%2==0])

#Exercise4
#I'll get back to this

#Exercise5
#I'll get back to this

#Exercise6
array_count9 = lambda nums: len([x for x in nums if x ==9])

#Exercise7
array_front9 = lambda nums: bool(len([x for x in nums if x ==9])) if len(nums) <=4 else bool(len([x for x in nums[:4] if x ==9]))

#Exercise8
array123 = lambda nums: set([1,2,3]).issubset(nums)

#Exercise9
#I'll get back to this
