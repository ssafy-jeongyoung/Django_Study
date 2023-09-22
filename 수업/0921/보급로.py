from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solve(s, e):
    dq = deque([])
    dq.append((s, e))
    while dq:
        cr, cc = dq.popleft()
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < N and 0 <= nc < N and weight_map[cr][cc] + road[nr][nc] < weight_map[nr][nc]:
                weight_map[nr][nc] = weight_map[cr][cc] + road[nr][nc]
                dq.append((nr, nc))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]

    weight_map = [[0xffffff] * N for _ in range(N)]
    weight_map[0][0] = 0

    solve(0, 0)
    print(f'#{tc} {weight_map[N-1][N-1]}')