n, m = map(int, input().split())

x, y, direction = map(int, input().split())

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

d = [[0]*m for _ in range(n)]
d[x][y] = 1

# 북,동,남,서 순서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left(direction):
  direction -= 1
  if direction == -1:
    direction = 3
  return(direction)

count = 1
turn_count = 0

while True:
  direction = turn_left(direction)
  nx = x + dx[direction]
  ny = y + dy[direction]
  
  # 회전하고 가보지 않은 칸이나 육지일 때
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_count = 0
    continue

  # 회전하고 가보지 않은 칸이 없거나 바다 일 때
  else:
    turn_count += 1

  # 네 방향 모두 갈 수 없는 경우
  if turn_count == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    # 뒤로 갈 수 있는 경우
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀 있는 경우
    else:
      break

    turn_count = 0

print(count)
  
  

