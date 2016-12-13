#Exercise1
sleep_in = lambda weekday, vacation: (not weekday) or (vacation)

#Exercise2
monkey_trouble = lambda a_smile, b_smile: (a_smile and b_smile) or (not a_smile and not b_smile)

#Exercise3
sum_double = lambda a, b: a+b if a != b else 2*(a+b)

#Exercise4
diff21 = lambda n: abs(21-n) if n <=21 else 2*abs(21-n)

#Exercise5
parrot_trouble = lambda talking, hour: talking and (hour < 7 or hour >20)

#Exercise6
makes10 = lambda a, b: (a==10 or b==10) or (a+b==10)

#Exercise7
near_hundred = lambda n: abs(200-n)<=10 or abs(100-n)<=10

#Exercise8
pos_neg = lambda a, b, negative: (not negative and ((a >= 0 and b < 0) or (a < 0 and b >= 0))) or (negative and a < 0 and b < 0)

#Exercise9
not_string = lambda str: str if (str == 'not' or 'not ' in str) else "not {0}".format(str)

#Exercise10
missing_char = lambda str, n: "{0}{1}".format(str[:n],str[n+1:])

#Exercise11
front_back = lambda str: str[::-1] if len(str) <=2 else "{2}{1}{0}".format(str[0],str[1:-1],str[-1])

#Exercise12
front3 = lambda str: str*3 if len(str)<=3 else str[0:3]*3
