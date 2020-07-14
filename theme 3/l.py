a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == abs(b - d) or a == c or b == d:
    print('YES')
else:
    print('NO')