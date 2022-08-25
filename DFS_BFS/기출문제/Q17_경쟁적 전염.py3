import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
array = []

# 서, 동, 북, 남
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    array.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

virus = []
for i in range(n):
  for j in range(n):
    if array[i][j] != 0:
      virus.append((array[i][j], i, j))

virus.sort()

def bfs(virus):
  q = deque()
  for i in virus:
    q.append(i)
  count = 0
  prev_virus = 0
  while q:
    new_virus, x, y = q.popleft()
    if new_virus < prev_virus:
      count += 1
    if count == s:
      break              
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (0 <= nx < n) & (0 <= ny < n):
        if array[nx][ny] == 0:
          array[nx][ny] = new_virus
          q.append((new_virus, nx, ny))
          prev_virus = new_virus
    
bfs(virus)
print(array[x-1][y-1])