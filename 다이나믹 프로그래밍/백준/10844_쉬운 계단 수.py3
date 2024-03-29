import sys

n = int(sys.stdin.readline())
array = [[0]*10 for _ in range(n)]
array[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
  for j in range(10):
    if j == 0:
      array[i][j] = array[i-1][j+1] 
    elif j == 9:
      array[i][j] = array[i-1][j-1] 
    else:
      array[i][j] = array[i-1][j+1] + array[i-1][j-1]

print(sum(array[-1]) % 1000000000)