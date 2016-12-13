#Exercise1
cigar_party = lambda cigars, is_weekend: (40 <=cigars <= 60 and not is_weekend) or (40 <=cigars and is_weekend)

#Exercise2
date_fashion = lambda you, date: 2 if ((you >=8 and date >2) or (date >=8 and you >2)) else (0,1)[you > 2 and date > 2]

#Exercise3
squirrel_play = lambda temp, is_summer: (not is_summer and 60 <= temp <= 90) or (is_summer and 60 <= temp <= 100)

#Exercise4
caught_speeding= lambda speed, is_birthday: 0 if (not is_birthday and speed <= 60) or (is_birthday and speed <= 65) else (2,1)[(not is_birthday and speed <= 80) or (is_birthday and speed <= 85)]

#Exercise5
sorta_sum = lambda a, b: a+b if not (10 <= a+b <= 19) else 20

#Exercise6
alarm_clock = lambda day, vacation: 'off' if vacation and (day==0 or day==6) else ('7:00','10:00') [vacation or (not vacation and (day==0 or day==6))]

#Exercise7
love6 = lambda a, b: a==6 or b==6 or a+b==6 or abs(a-b)==6

#Exercise8
in1to10 = lambda n, outside_mode: ((1 <= n <= 10) and not outside_mode) or ((1>=n or n >= 10) and outside_mode)
