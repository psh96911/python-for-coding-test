import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

data.sort()
count = 0
left = 0
right = n-1

while left < right:
  if data[left] + data[right] < x:
    left += 1

  elif data[left] + data[right] > x:
    right -= 1

  elif data[left] + data[right] == x:
    left += 1
    right -= 1
    count += 1

print(count)