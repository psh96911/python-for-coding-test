import sys
input = sys.stdin.readline

n = int(input())
graph=[]
for _ in range(n):
  a = list(map(int, input().split()))
  graph.append(a)


for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k]+graph[k][j] == 2:
        graph[i][j] = 1

for i in range(n):
  for j in range(n):
    print(graph[i][j], end=" ")
  print()
