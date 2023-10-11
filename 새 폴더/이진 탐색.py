def binary(lst, n, target):
    s = 0
    e = n - 1
    flag = 0
    while s <= e:
        m = (s + e)//2
        if lst[m] == target:
            return 1
        elif lst[m] > target:
            if flag != -1:
                e = m-1
                flag = -1
            else:
                return 0
        elif lst[m] < target:
            if flag != 1:
                s = m+1
                flag = 1
            else:
                return 0
    return 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        ans += binary(A, N, B[i])

    print(f'#{tc} {ans}')