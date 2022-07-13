n = int(input())
plans = input().split()

x, y = 1, 1
move_types = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in plans:
  for j in range(len(move_types)):
    if i == move_types[j]:
      nx = x + dx[j]
      ny = y + dy[j]
  if (1<=nx & nx<=n) & (1<=ny & ny<=n):
    x, y = nx, ny
    
print(x,y)
