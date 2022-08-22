import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [-1]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

def bfs(graph, start, distance):
  queue = deque([start])
  distance[start] = 0

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if distance[i] == -1:
        distance[i] = distance[v] + 1
        queue.append(i)
      
bfs(graph, x, distance)

if k not in distance:
    print(-1)
else:
  for i in range(n+1):
    if distance[i] == k:
      print(i)