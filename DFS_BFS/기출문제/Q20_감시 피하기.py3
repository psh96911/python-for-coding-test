from itertools import combinations
from collections import deque
from copy import deepcopy

n = int(input())
array = []
teacher = []
blank = []

# 서, 동, 북, 남
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
  array.append(list(input().split()))
  for j in range(n):
    if array[i][j] == 'T':
      teacher.append((i, j))
    elif array[i][j] == "X":
      blank.append((i, j)) 

def bfs(array): # 학생 찾으면 False 반환
  graph = deepcopy(array)
  q = deque(teacher)
  while q:
    x, y = q.popleft()
    for i in range(4):
      input_x, input_y = x, y
      while True: # 한 방향으로 False 나올때까지 이동 
        nx, ny = input_x + dx[i], input_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
          if graph[nx][ny] == 'X':
            graph[nx][ny] = 'T'
          elif graph[nx][ny] == 'S':
            return False
          elif graph[nx][ny] == 'O':
            break
          input_x, input_y = nx, ny
        else:
          break       
  return True

obstacle = list(combinations(blank, 3))

result = False
for obs in obstacle:
  for x, y in obs:
    array[x][y] = 'O'
  if bfs(array):
    result = True
    break
  for x, y in obs:
    array[x][y] = 'X'
    
if result:
  print("YES")
else:
  print("NO")