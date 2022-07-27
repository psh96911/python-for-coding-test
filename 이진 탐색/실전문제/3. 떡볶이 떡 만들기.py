n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0
while True:
  total = 0
  mid = (start+end)//2
  for i in data:
    if i > mid:
      total += (i-mid)

  if total > m:
    start = mid+1
  elif total < m:
    end = mid-1
  else:
    result = mid
    break

print(result)
  