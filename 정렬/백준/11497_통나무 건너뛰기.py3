import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  data = list(map(int, sys.stdin.readline().split()))
  data.sort()

  result = 0
  for i in range(2, n):
    result = max(result, abs(data[i]-data[i-2]))
    
  print(result)