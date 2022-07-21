from collections import deque

n, k = map(int, input().split())
data =[0] * (100001)

def bfs(n, k):
  q = deque([n])
  while q:
    x = q.popleft()
    
    if x == k:
      print(data[x])
      break

    for i in (x-1, x+1, 2*x):
      if  0<=i<=100000 and data[i] == 0:
        data[i] = data[x] + 1
        q.append(i)

bfs(n,k)