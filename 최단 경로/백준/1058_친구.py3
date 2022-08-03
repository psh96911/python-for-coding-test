import sys
input = sys.stdin.readline

n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]

for _ in range(n):
  a = list(input().rstrip())
  graph.append(a)

for k in range(n):
  for a in range(n):
    for b in range(n):
      if a == b:
        continue
      if graph[a][b] =='Y' or (graph[a][k] == 'Y' and graph[k][b] == 'Y'):
        visited[a][b] = 1

result = 0
for i in visited:
  result = max(result, sum(i))
 
print(result)