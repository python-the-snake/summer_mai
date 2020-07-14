a = int(input())
if a == 1:
    print(a, 'korova')
elif a >= 11 and a <= 14:
    print(a, 'korov')
elif a % 10 == 1:
    print(a, 'korova')
elif a % 10 >=2 and a % 10 <= 4:
    print(a, 'korovy')
else:
    print(a, 'korov')