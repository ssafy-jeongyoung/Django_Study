from collections import deque

def bfs(row, col):
    global ans
    dq = deque()
    dq.append((row, col))

    while dq:
        cr, cc = dq.popleft()
        
    return dq


M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

# 새 박스 리스트를 만들고 box를 하나하나 탐색해서 1의 인접 위치는 새박스에 1로 저장
# 처음 탐색 때 flag를 True로 넣고 0이 하나라도 발견되면 False로 반환하여 0을 출력(ans = 1일 때)
# ans가 2이상이면 flag를 종료조건으로 사용


a = bfs(0, 0)
print(a)