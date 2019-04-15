#!/usr/bin/env python3

def countingValleys(n, s):
    steps = list(s)
    result = 0
    count = 0
    temp = []
    for step in steps:
        if step == "U":
            count += 1
            temp.append(count)
        elif step == "D":
            count -= 1
            temp.append(count)
    temp_temp = []
    for index, dif in enumerate(temp):
    	if dif == 0:
    		temp_temp.append(index -1)
    for i in temp_temp:
    	if temp[i] < 0:
    		result +=1 
    return result



print(countingValleys(8,"DDUUDDUDUUUD"))