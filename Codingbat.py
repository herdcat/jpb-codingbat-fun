class Solutions(object):
    #Exercise1
    first_last6 = lambda self, nums: (nums[0]==6) or (nums[-1]==6)

    #Exercise2
    same_first_last = lambda self, nums: nums[0]==nums[-1] if len(nums)>0 else False

    #Exercise3
    make_pi = lambda self: [3,1,4]

    #Exercise4
    common_end = lambda self, a, b: (a[0]==b[0]) or (a[-1]==b[-1])

    #Exercise5
    sum3 = lambda self, nums: sum(nums)

    #Exercise6
    rotate_left3 = lambda self, nums: [nums[1],nums[2],nums[0]]

    #Exercise7
    reverse3 = lambda self, nums: nums[::-1]

    #Exercise8
    max_end3 = lambda self, nums: [nums[0]]*3 if nums[0]>=nums[-1] else [nums[-1]]*3

    #Exercise9
    sum2 = lambda self, nums: sum(nums[:2])

    #Exercise10
    middle_way = lambda self, a, b: [a[1],b[1]]

    #Exercise11
    make_ends = lambda self, nums: [nums[0],nums[-1]]

    #Exercise12
    has23 = lambda self, nums: 2 in nums or 3 in nums

    #Exercise1
    count_evens = lambda self, nums: len([x for x in nums if x % 2 ==0])

    #Exercise2
    big_diff = lambda self, nums: max(nums) - min(nums)

    #Exercise3
    centered_average = lambda self, nums: sum(sorted(nums)[1:-1])/len(sorted(nums)[1:-1])

    #Exercise4
    sum13 = lambda self, nums: sum([x for i,x in enumerate(nums) if (nums[i-1]!=13 and nums[i]!=13 and i!=0) or ((nums[i]!=13) and i==0)])

    #Exercise5
    #Will come back to this

    #Exercise6
    has22 = lambda self, nums: "22" in "".join(["{0}".format(x) for x in nums])

    #Exercise1
    cigar_party = lambda self, cigars, is_weekend: (40 <=cigars <= 60 and not is_weekend) or (40 <=cigars and is_weekend)

    #Exercise2
    date_fashion = lambda self, you, date: 2 if ((you >=8 and date >2) or (date >=8 and you >2)) else (0,1)[you > 2 and date > 2]

    #Exercise3
    squirrel_play = lambda self, temp, is_summer: (not is_summer and 60 <= temp <= 90) or (is_summer and 60 <= temp <= 100)

    #Exercise4
    caught_speeding= lambda self, speed, is_birthday: 0 if (not is_birthday and speed <= 60) or (is_birthday and speed <= 65) else (2,1)[(not is_birthday and speed <= 80) or (is_birthday and speed <= 85)]

    #Exercise5
    sorta_sum = lambda self, a, b: a+b if not (10 <= a+b <= 19) else 20

    #Exercise6
    alarm_clock = lambda self, day, vacation: 'off' if vacation and (day==0 or day==6) else ('7:00','10:00') [vacation or (not vacation and (day==0 or day==6))]

    #Exercise7
    love6 = lambda self, a, b: a==6 or b==6 or a+b==6 or abs(a-b)==6

    #Exercise8
    in1to10 = lambda self, n, outside_mode: ((1 <= n <= 10) and not outside_mode) or ((1>=n or n >= 10) and outside_mode)

    #Exercise9
    near_ten = lambda self, num: (num % 10 <=2) or (8 <= num % 10 <=9)

    #Exercise1
    make_bricks = lambda small, big, goal: True if ((goal % 5 == 0 and goal/5<=big) or (goal <= small)) else [False,True][(((goal - (goal/5)*5) <= small) and ((goal/5) <= big)) or (((goal - (big*5)) <= small) and (goal - (big*5) >= 0))]

    #Exercise2
    lone_sum = lambda a, b, c: [[a,[b,[c,0][c==a or c==b]][b==a or b==c]][a==b or a==c],a+b+c][(a != b != c) and a != c]

    #Exercise3
    lucky_sum = lambda a, b, c: a+b+c if (a!=13 and b!=13 and c!=13) else[0,[a,a+b][b!=13]][a!=13]

    #Exercise4
    no_teen_sum = lambda a, b, c: sum([x for x in [a,b,c] if (x<=12 or x>=20) or (x==15 or x==16)])

    #Exercise5
    round_sum = lambda a, b, c: int(sum([round(float(x)/10)*10 for x in [a,b,c]]))

    #Exercise6
    close_far = lambda a, b, c: (abs(a-b) <=1 and abs(a-c) >=2 and abs(b-c) >=2 ) or ( abs(a-b) >=2 and abs(c-b) >=2 and abs(a-c) <=1 )

    #Exercise7
    make_chocolate = lambda small, big, goal: [[[[[-1,goal-(big*5)][goal-(big*5)<=small and goal-(big*5)>=0],goal-((goal/5)*5)][goal-((goal/5)*5)<=small and goal/5 <= big],goal-(goal/5)*5][goal < 5 and goal <= small],0][goal%5==0 and goal/5 <= big],goal][goal < 5 and goal <= small]

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

