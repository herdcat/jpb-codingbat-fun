#Exercise1
string_times = lambda str, n: str*n

#Exercise2
front_times = lambda str, n: str*n if len(str)<=3 else str[0:3]*n

#Exercise3
string_bits = lambda str: "".join([x for i, x in enumerate(str) if i%2==0])

#Exercise4
string_splosion = lambda str: "".join([str[:i+1] for i, x in enumerate(str) if i < len(str)])

#Exercise5
last2 = lambda str: len([i for i,x in enumerate(str) if (str[i:i+2]==str[-2:])])-1 if len(str) > 0 else 0

#Exercise6
array_count9 = lambda nums: len([x for x in nums if x ==9])

#Exercise7
array_front9 = lambda nums: bool(len([x for x in nums if x ==9])) if len(nums) <=4 else bool(len([x for x in nums[:4] if x ==9]))

#Exercise8
array123 = lambda nums: set([1,2,3]).issubset(nums)

#Exercise9
string_match = lambda a, b: len([x for i,x in enumerate(a) if (a[i]==b[i]) and a[i-1]==b[i-1] and i<len(a) and i!=0]) if len(a) <= len(b) else len([x for i,x in enumerate(b) if (a[i]==b[i] and a[i-1]==b[i-1] and i<len(b) and i!=0)])
