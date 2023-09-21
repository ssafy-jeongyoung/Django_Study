def solve(start, team):
    stack = [start]
    visited[stack[-1]] = 1
    team.append(stack[-1])
    while stack:
        for s in range(1, N+1):
            if adj[stack[-1]][s] == 1 and not visited[s]:
                stack.append(s)
                visited[s] = 1
                team.append(stack[-1])
                break
        else:
            stack.pop()
    return team


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 사람 수
    # M : 신청서 수 (x,y)

    arr = list(map(int, input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        adj[arr[i]][arr[i+1]] = 1
        adj[arr[i+1]][arr[i]] = 1

    visited = [0] * (N+1)
    ans_lst = []
    for i in range(2*M):
        if visited[arr[i]] == 0:
            a = solve(arr[i], [])
            if a not in ans_lst:
                ans_lst.append(a)
            visited[arr[i]] = 1
    l = len(ans_lst)
    for i in range(1, N+1):
        if visited[i] == 0:
            l += 1
    print(f'#{tc} {l}')
