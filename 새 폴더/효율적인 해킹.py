import sys


def solve(row):
    queue = [row]
    visited[row] = 1
    cnt = 1
    while queue:
        cr = queue.pop(0)
        for k in range(1, N+1):
            if not visited[k] and k in computer[cr]:
                queue.append(k)
                visited[k] = 1
                cnt += 1
    return cnt, row


N, M = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
computer = dict()
for i in range(1, N+1):
    computer[i] = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    computer[b].append(a)

com = dict()
for i in range(1, N+1):
    c, r = solve(i)
    com[r] = c

ans = [k for k, v in com.items() if max(com.values()) == v]
print(*ans)
