number = int(input())
k = number % 10
n = number % 100 // 10
s = number // 100 % 10
c = number // 1000
print (10* (k-c)+ (n-s) +1)