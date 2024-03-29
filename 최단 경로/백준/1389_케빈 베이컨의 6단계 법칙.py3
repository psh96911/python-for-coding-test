import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b= map(int, input().split())
  if a==b:
    graph[a][b] = 0
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = []
bacon = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] != INF:
      bacon += graph[i][j]
  result.append((bacon,i))
  bacon = 0

result.sort()
print(result[0][1])