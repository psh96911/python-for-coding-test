n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)


def dfs(graph, v, visited):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(graph, i, visited)
  return sum(visited)-1

print(dfs(graph, 1, visited))