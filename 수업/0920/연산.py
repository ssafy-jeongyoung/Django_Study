def bfs(n, m, cnt):
    queue = [(n, cnt)]
    visited = [0] * 2222222
    visited[n] = 1
    while queue:
        cn, ccnt = queue.pop(0)
        if cn == m:
            return ccnt
        if cn > 1000000:
            continue

        if not visited[cn + 1]:
            queue.append((cn+1, ccnt+1))
            visited[cn + 1] = 1
        if not visited[cn - 1]:
            queue.append((cn - 1, ccnt + 1))
            visited[cn - 1] = 1
        if not visited[cn - 10]:
            queue.append((cn - 10, ccnt + 1))
            visited[cn - 10] = 1
        if not visited[cn * 2]:
            queue.append((cn * 2, ccnt + 1))
            visited[cn * 2] = 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    while N != M:
        if N > M:
            if N-M < 6:
                N = M
                ans += N-M
            else:
                N -= 10
                ans += 1
        else:
            a = bfs(N, M, ans)
            N = M
            ans = a
    print(f'#{tc} {ans}')