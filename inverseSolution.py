#我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
#今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
#输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
#注：所给数据都有解，不用考虑无解的情况。
a = 8
b = 144
sum_m_n = []
k = max(a,b) / min(a,b)

for i in range(1,k + 1):
    for j in range(1,k + 1):
        m = i * min(a,b)
        n = j * min(a,b)
        if i * j == k and m < n:
            sum_m_n.append(m + n)

for i in range(1,k + 1):
    for j in range(1,k + 1):
        m = i * min(a,b)
        n = j * min(a,b)
        if i * j == k and m < n and m + n == min(sum_m_n):
            print m,n
