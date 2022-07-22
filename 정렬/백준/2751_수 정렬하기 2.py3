import sys

n = int(sys.stdin.readline())

data = []

for i in range(n):
  a = int(sys.stdin.readline())
  data.append(a)

data.sort()

for i in range(n):
  print(data[i])
