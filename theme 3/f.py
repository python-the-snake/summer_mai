a = int(input())
b = int(input())
c = int(input())
if (a + b <= c) or (a + c <= b) or (b + c <= a) :
    print('NO')
else:
    print('YES')