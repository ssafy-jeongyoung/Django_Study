N = int(input())

lst = []
for i in range(N):
    num, name = input().split()
    lst.append((int(num), i, name))

lst.sort()
for i in range(N):
    print(f'{lst[i][0]} {lst[i][2]}')
