from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(r, c):
    dq = deque([])
    dq.append((r, c))

    while dq:
        cr, cc = dq.popleft()
        if weight_map[cr][cc] != 0xffffff and weight_map[cr][cc] + (N-1-cr + N-1-cc) >= weight_map[N-1][N-1]:
            continue
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] > field[cr][cc] and weight_map[cr][cc] + (field[nr][nc] - field[cr][cc]) + 1 < weight_map[nr][nc]:
                    dq.append((nr, nc))
                    weight_map[nr][nc] = weight_map[cr][cc] + (field[nr][nc] - field[cr][cc]) + 1
                elif field[nr][nc] <= field[cr][cc] and weight_map[cr][cc] + 1 < weight_map[nr][nc]:
                    dq.append((nr, nc))
                    weight_map[nr][nc] = weight_map[cr][cc] + 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    weight_map = [[0xffffff] * N for _ in range(N)]
    weight_map[0][0] = 0

    bfs(0, 0)

    print(f'#{tc} {weight_map[N-1][N-1]}')