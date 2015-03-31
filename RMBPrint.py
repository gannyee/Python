
import math

transfer = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
unit =['','拾','佰','仟','万']
b = []
b.append('圆')
def trans(c):
    flage = 0
    while c and flage <= 4:
        
        
            
        b.append(unit[flage])
        b.append(transfer[c % 10])
        
        flage = flage + 1
        while flage > 4:
            flage = 1
        
        c = c / 10
    
c = abs(a)

if c == 0:
    b.append(transfer[0])
else:
    trans(c)
if a < 0:
    b.append('负')
s = ''
s = "".join(b[::-1])

for k in range(3):
	m=len(s)
	for i in range(m/3):
		if s[3*i:3*(i+1)]=='零':
			if s[3*(i+1):3*(i+2)]=='仟' or s[3*(i+1):3*(i+2)]=='佰' or s[3*(i+1):3*(i+2)]=='拾' or s[3*(i+1):3*(i+2)]=='零':
				s=s[0:3*(i+1)]+s[3*(i+2):m]
		elif s[3*i:3*(i+1)]=='万' and s[3*(i-1):3*i]=='零':
			s=s[0:3*(i-1)]+s[3*i:m]
		elif s[3*i:3*(i+1)]=='圆' and s[3*(i-1):3*i]=='零' and m!=6:
			s=s[0:3*(i-1)]+s[3*i:m]

print s
