#Exercise1
hello_name = lambda name: "Hello {0}!".format(name)

#Exercise2
make_abba = lambda a, b: "{0}{1}{1}{0}".format(a,b)

#Exercise3
make_tags = lambda tag, word: "<{0}>{1}</{0}>".format(tag,word)

#Exercise4
make_out_word = lambda out, word: "{0}{1}{2}".format(out[:2],word,out[2:])

#Exercise5
extra_end = lambda str:str[-2:]*3

#Exercise6
first_two = lambda str: str if len(str) <3 else str[:2]

#Exercise7
first_half = lambda str: str[:(len(str)/2)]

#Exercise8
without_end = lambda str: str[1:-1]

#Exercise9
combo_string = lambda a, b: "{0}{1}{0}".format(a,b) if len(a) < len(b) else "{1}{0}{1}".format(a,b)

#Exercise10
non_start = lambda a, b: "{0}{1}".format(a[1:],b[1:])

#Exercise11
left2 = lambda str: "{0}{1}".format(str[2:],str[:2])

#Exercise12
