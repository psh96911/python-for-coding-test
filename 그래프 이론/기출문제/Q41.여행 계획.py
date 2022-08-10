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

for i in range(1, n+1):
  parent[i] = i

graph = []
for i in range(1, n+1):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      graph.append((i,j+1))

for i in graph:
  a, b = i
  union_parent(parent, a, b)

plan = list(map(int, input().split()))

result = find_parent(parent, plan[0])
count = 0
for i in plan:
  count += 1
  if result != find_parent(parent, i):
    print("NO")
    break

if count == len(plan):
  print("YES")
  