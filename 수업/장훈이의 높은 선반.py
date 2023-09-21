def solve(sum_v, i):
    global min_v
    if sum_v < 0:
        return

    if i == -1:
        if sum_v < min_v:
            min_v = sum_v
        return

    solve(sum_v-H[i], i-1)
    solve(sum_v, i-1)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split()) # B : 탑의 목표 높이
    H = list(map(int, input().split()))  # N명 각각의 키
    H.sort()
    min_v = sum(H)-B
    solve(sum(H)-B, N-1)

    print(f'#{tc} {min_v}')