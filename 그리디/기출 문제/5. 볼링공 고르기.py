n, m = map(int, input().split())
data = list(map(int, input().split()))


array = [0] * 11

for i in data:
  array[i] += 1


count = 0

for i in range(1, m+1):
  n -= array[i]
  count += array[i] * n

print(count)


