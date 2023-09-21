def solve(visit, sum_v, v):   # v : 제품
    global min_v
    if sum_v > min_v:
        return

    if v == N:
        if min_v > sum_v:
            min_v = sum_v
        return
    for p in range(N):  # 공장
        if not visit[p]:
            visit[p] = 1
            solve(visit, sum_v+arr[v][p], v+1)
            visit[p] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N  # 공장
    min_v = 10000
    solve(visited, 0, 0)
    print(f'#{tc} {min_v}')

