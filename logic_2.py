#Exercise1
#Figuring out how to do this in one line

#Exercise2
lone_sum = lambda a, b, c: [[a,[b,[c,0][c==a or c==b]][b==a or b==c]][a==b or a==c],a+b+c][(a != b != c) and a != c]

#Exercise3
lucky_sum = lambda a, b, c: a+b+c if (a!=13 and b!=13 and c!=13) else[0,[a,a+b][b!=13]][a!=13]

#Exercise4

#Exercise5

#Exercise6
close_far = lambda a, b, c: (abs(a-b) <=1 and abs(a-c) >=2 and abs(b-c) >=2 ) or ( abs(a-b) >=2 and abs(c-b) >=2 and abs(a-c) <=1 )
