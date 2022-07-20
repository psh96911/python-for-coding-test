from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()


def dfs(graph, v, visited):
  visited[v] = 1
  print(v, end=" ")
  for i in graph[v]:
    if visited[i] ==0:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = 1
  while q:
    v = q.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = 1

dfs(graph, v, visited)
visited = [0] * (n+1)
print()
bfs(graph, v, visited)