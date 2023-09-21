# 다익스트라 알고리즘
def dijkstra(start):
    weight = graph[start][:]
    # 정점까지 가는 비용이 확정된 정점의 목록
    selected = set()
    weight[start] = 0
    # 모든 정점에 대해 비용이 확정될 때 까지 반복
    while len(selected) < V:
        min_weight = 0xfffffff
        min_node = -1
        for i in range(V):
            if i not in selected and weight[i] < min_weight:
                min_node = i
                min_weight = weight[i]
        # 최소 비용으로 갈 수 있는 정점이 선택됨
        selected.add(min_node)

        # min_node를 통해 갈 수 있는 새로운 경로에 대한 비용
        # min_node까지 가는 비용 + min_node에서 다른 노드로 가는 비용
        for i in range(V):
            # weight[i] vs min_weight + graph[min_node][i]
            if i not in selected:
                weight[i] = min(weight[i], min_weight + graph[min_node][i])

    return weight


V, E = map(int, input().split())
graph = [0xffffffff] * V

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w

    answer = dijkstra(0)
    print(answer)
