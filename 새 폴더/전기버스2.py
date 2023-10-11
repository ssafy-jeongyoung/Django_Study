T = int(input())

for tc in range(1, T+1):
    lst = input().split()
    N = int(lst[0])
    Mi = [0] + [int(lst[i]) for i in range(1, N)]
    ans = 0
    mini_stop = N
    while True:
        j = mini_stop
        for i in range(mini_stop-1, -1, -1):
            if i + Mi[i] >= j:
                mini_stop = i
        ans += 1
        if mini_stop <= Mi[1]+1:
            break

    print(f'#{tc} {ans}')