注明：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
注意：由于中文乱码问题，输出时请先decode("utf8")，例如你要输出ans = "零圆", print ans.decode("utf8").
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示

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
