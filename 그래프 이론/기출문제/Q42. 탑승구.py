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

g = int(input())
p = int(input())

parent = [0]*(g+1)
for i in range(1, g+1):
    parent[i] = i

data = []
for _ in range(p):
  n = int(input())
  data.append(n)

count = 0
for i in data:
  x = find_parent(parent, i)
  if x == 0 :
    print(count)
    break
  count += 1
  union_parent(parent, x, x-1)