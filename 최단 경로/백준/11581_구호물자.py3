import sys
input = sys.stdin.readline


n = int(input())
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(1, n):
  a = int(input())
  b = list(map(int, input().split()))
  for j in b:
    graph[i][j] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if graph[a][k] == 1 and graph[k][b] == 1:
        graph[a][b] = 1

count = 0
Break = False
for a in range(1, n):
  count += 1
  for b in range(1, n):
    if graph[a][b] == 1 and graph[b][a] == 1 and (graph[1][a] == 1 or graph[1][b] == 1):
      print("CYCLE")
      Break = True
      break
  if Break:
    break
  elif count == n-1:
    print("NO CYCLE")