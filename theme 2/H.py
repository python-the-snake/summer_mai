a = int(input())
b = int(input())
c = int(input())
max = a
if b > max:
    max = b
if c > max:
    max = c
print(max)
[16:09]
Тема 3 Задача E
-----------------------------------------------------
[16:16]
den = int(input())
ira = int(input())
if (den == 1 and ira == 1) or (den != 1 and ira != 1):
    print('YES')
else:
    print('NO')