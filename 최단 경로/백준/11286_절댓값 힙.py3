import heapq
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
  x = int(input())
  array.append((abs(x),x))

q = []
for i in range(n):
  if array[i][1] != 0:
    heapq.heappush(q, array[i])
  else:
    print(heapq.heappop(q)[1] if q else 0)