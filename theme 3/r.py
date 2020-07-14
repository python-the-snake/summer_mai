N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N > M:
    N, M = M, N
print (min(x, N - x, y, M - y))