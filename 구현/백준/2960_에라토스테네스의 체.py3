import sys

n, k = map(int, sys.stdin.readline().split())

data = [i for i in range(2,n+1)]

count = 0

while count < k:
  p = min(data)
  for i in data:
    if i%p == 0:
      data.remove(i)
      count += 1
      if count == k:
        print(i)
        break