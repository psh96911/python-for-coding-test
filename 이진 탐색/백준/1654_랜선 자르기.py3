import sys

k, n = map(int, sys.stdin.readline().split())
array = []
for i in range(k):
  a = int(sys.stdin.readline())
  array.append(a)


start = 1
end = max(array)

result = 0
while start <= end:
  mid = (start+end)//2
  total = 0
  for x in array:
    total += (x // mid)

  if total < n:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)