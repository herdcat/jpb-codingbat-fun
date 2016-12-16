#Exercise1
double_char = lambda str: "".join([x*2 for x in str])

#Exercise2
count_hi = lambda str: str.count('hi')

#Exercise3
cat_dog = lambda str: str.count('cat') == str.count('dog')

#Exercise4
#Coming back to this later

#Exercise5
end_other = lambda a, b: a.lower()[-len(b):] == b.lower() if len(a) >= len(b) else b.lower()[-len(a):] == a.lower()

#Exercise6
xyz_there = lambda str: bool(str.replace('.xyz','').count('xyz'))
