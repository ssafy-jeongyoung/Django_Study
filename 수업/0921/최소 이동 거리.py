from collections import deque

def solve(start):
    dq = deque([])
    dq.append(start)
    while dq:
        s = dq.popleft()
        for i in range(N+1):
            if graph[s][i] and distance[i] > distance[s] + graph[s][i]:
                dq.append(i)
                distance[i] = distance[s] + graph[s][i]


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        x, y, w = map(int, input().split())
        graph[x][y] = w

    distance = [0xfffffff] * (N+1)
    distance[0] = 0

    solve(0)
    print(f'#{tc} {distance[N]}')