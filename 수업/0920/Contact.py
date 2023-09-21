def bfs(sizak):
    queue = [sizak]
    visited = [0] * 101
    visited[sizak] = 1

    while queue:
        n = queue.pop(0)

        for k in range(1, 101):
            if not visited[k] and graph[n][k] == 1:
                queue.append(k)
                visited[k] = visited[n] + 1

    max_v = max(visited)
    for re in range(100, -1, -1):
        if visited[re] == max_v:
            return re


for tc in range(1, 11):
    L, start = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [[0] * 101 for _ in range(101)]

    for i in range(0, L, 2):
        graph[lst[i]][lst[i + 1]] = 1

    print(f'#{tc} {bfs(start)}')
