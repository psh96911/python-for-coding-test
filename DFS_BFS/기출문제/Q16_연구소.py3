import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
array = []

# 서, 동, 북, 남
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    array.append(list(map(int, input().split())))

def virus(graph, a, b):
  q = deque()
  q.append((a,b))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (0 <= nx < n) & (0 <= ny < m):
        if graph[nx][ny] == 0:
          graph[nx][ny] = 2
          q.append((nx, ny))
                  
def bfs(array, walls):
  graph = deepcopy(array)
  
  for a, b in walls:
    graph[a][b] = 1

  for a in range(n):
    for b in range(m):
      if graph[a][b] == 2:
        virus(graph, a, b)

  count = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        count += 1

  return count
 
not_wall = []
for i in range(n):
  for j in range(m):
    if array[i][j] == 0:
      not_wall.append((i,j))

new_walls = list(combinations(not_wall, 3))

ans = 0
for walls in new_walls:
  bfs_result = bfs(array, walls)
  ans = max(ans, bfs_result)
  
print(ans)