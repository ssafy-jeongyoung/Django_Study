def dfs(start):
    for c in range(H+2):

    return


N, M, H = map(int, input().split())

sadari = [[0]*(N+1) for _ in range(H+2)]

ans = 0
if M > 0:
    for i in range(M):
        a, b = map(int, input().split())
        sadari[a][b] = 1
        sadari[a][b+1] = 1





elif M == 0:
    print(ans)
