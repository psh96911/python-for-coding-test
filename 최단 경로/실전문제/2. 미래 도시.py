import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 각 노드의 연결되어 있는 노드에 대한 정보를 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 모든 간선 정보 입력받기
for _ in range(m):
  # a번 노드에서 b번 노드로 가는 비용이 1
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1


# 거쳐 갈 노드 K와 최종 목적지 노드 X를 입력 받기
x, k = map(int, input().split())
  
# 점화식에 따라 플로이드 위셜 알고리즘을 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] +graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)