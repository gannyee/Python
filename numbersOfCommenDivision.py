#给你两个正整数a,b,  输出它们公约数的个数。

a = 4483378
b = 884324
def divisionCount(s):
    division = []
    for i in range(1,s + 1):
        if s % i == 0:
            division.append(i)
    return division
    
def CommenDivision(a,b):
    count = 0
    for i in a:
        for j in b:
            if i == j:
                count += 1
    return count


print CommenDivision(divisionCount(a),divisionCount(b))
