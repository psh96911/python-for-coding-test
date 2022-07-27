n = int(input())
array = list(map(int, input().split())) 
m = int(input())

start = 0
end = max(array)

result = 0
while start<=end:
  mid = (start+end)//2
  total = 0
  for x in array:
    if x > mid:
      total += mid
    else:
      total += x

  if total > m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)