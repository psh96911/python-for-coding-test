import heapq

n = int(input())

array = []
for i in range(n):
  a = int(input())
  heapq.heappush(array, a)

result = 0
sum = 0

while len(array) != 1:
  a = heapq.heappop(array)
  b = heapq.heappop(array)

  sum = a + b
  result += sum
  heapq.heappush(array, sum)

print(result)