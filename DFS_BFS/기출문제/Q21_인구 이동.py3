import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

# 서, 동, 북, 남
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, array):
  q = deque()
  q.append((a,b))
  visitied[a][b] = 1
  pop_sum = array[a][b] # 총 인구수
  country = 1 # 연합국가 개수
  temp = [(a,b)] # 국경을 연 국가 위치
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (0<=nx<n) and (0<=ny<n):
        if (l <= abs(array[x][y] - array[nx][ny]) <= r) and (visitied[nx][ny] == 0):
          q.append((nx, ny))
          visitied[nx][ny] = 1
          country += 1
          pop_sum += array[nx][ny]
          temp.append((nx,ny))        
  for i,j in temp:
    array[i][j] = pop_sum // country

ans = 0
while True:
  count = 0
  visitied = [[0]*n for _ in range(n)]
  for a in range(n):
    for b in range(n):
      if visitied[a][b] == 0:
        bfs(a, b, array)
        count += 1
  if count == n*n:
    print(ans)
    break
  ans += 1