def solve(sum_v, v):
    global max_v
    if max_v > sum_v:
        return
    if v == N:
        if max_v < sum_v:
            max_v = sum_v
        return
    for p in range(N):
        if not visited[p] and P[v][p] != 0:
            visited[p] = 1
            solve(sum_v*(P[v][p]/100), v+1)
            visited[p] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    max_v = 0
    solve(1, 0)
    max_v *= 100
    print(f'#{tc} {max_v:.6f}')