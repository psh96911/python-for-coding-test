import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array_reverse = array[::-1]
d = [[1]*2 for _ in range(n)]

for i in range(1, n):
  if array[i] >= array[i-1]:
    d[i][0] = d[i-1][0] + 1
  if array[i] <= array[i-1]:
    d[i][1] = d[i-1][1] + 1

print(max(map(max, d)))