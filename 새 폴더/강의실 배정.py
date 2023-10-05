import sys
import heapq

N = int(sys.stdin.readline())
ans = 0
first = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(first, (a, b))

next = []
for i in first:
