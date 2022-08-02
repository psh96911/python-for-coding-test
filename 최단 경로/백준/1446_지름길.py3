import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

m, d = map(int, input().split())
graph = [[] for i in range(d+1)]
distance = [INF] * (d+1)

# 1,2,....d를 모든 노드로 간주
for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(m):
  a, b, c = map(int, input().split())
  if b > d:
    continue
  graph[a].append((b,c))

q = []
heapq.heappush(q,(0,0))
distance[0] = 0

while q: 
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) 

print(distance[d])
