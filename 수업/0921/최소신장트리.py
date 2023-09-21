T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0xfffffff]*(V+1) for _ in range(E)]

