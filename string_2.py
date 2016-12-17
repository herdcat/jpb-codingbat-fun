#Exercise1
double_char = lambda str: "".join([x*2 for x in str])

#Exercise2
count_hi = lambda str: str.count('hi')

#Exercise3
cat_dog = lambda str: str.count('cat') == str.count('dog')

#Exercise4
count_code = lambda str: len([x for i,x in enumerate(str) if (i < len(str)-3) and ((str[i:i+2]=='co') and str[i+3]=='e')])

#Exercise5
end_other = lambda a, b: a.lower()[-len(b):] == b.lower() if len(a) >= len(b) else b.lower()[-len(a):] == a.lower()

#Exercise6
xyz_there = lambda str: bool(str.replace('.xyz','').count('xyz'))
