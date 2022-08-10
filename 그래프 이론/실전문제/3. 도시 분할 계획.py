import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

# edges: 모든 간선 정보 / result:최종 비용
edges = []
result = []

for i in range(n+1):
  parent[i] = i

for i in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  # 싸이클이 발생하지 않은 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result.append(cost)

print(sum(result[:-1]))
    