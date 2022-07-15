n = int(input())
k = int(input())

data = [ [0]*(n+1) for _ in range(n+1) ]

for _ in range(k):
  row, col = map(int, input().split())
  data[row][col] = 1


info = []
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append([int(x),c])

# 동, 남, 서, 북
dx = [0, 1, 0 , -1]
dy = [1, 0, -1, 0]

# 방향 회전
def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return(direction)


x, y = 1, 1
data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
count = 0
direction = 0 # 동쪽에서 시작
turn_time = 0
q = [[x,y]] # 뱀이 차지하고 있는 위치

while True:
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
  if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny] != 2 :
    
    # 사과가 없다면
    if data[nx][ny] == 0:
      data[nx][ny] = 2
      q.append([nx,ny])
      px, py = q.pop(0)  # pop은 없앤 변수 저장 가능
      data[px][py] = 0
      
    elif data[nx][ny] == 1:
      data[nx][ny] = 2
      q.append([nx,ny])   

    x, y = nx, ny
    count += 1

  else:
    count += 1
    break
  
  if turn_time < l and info[turn_time][0] == count:
    direction = turn(direction, info[turn_time][1])
    turn_time += 1

print(count)
  
  


