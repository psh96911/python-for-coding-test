import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = max(array)
end = sum(array)

result = sys.maxsize
while start <= end:
  # mid: 블루레이 크기
  mid = (start + end) // 2
  # total: 한 블루레이 안에 들어가있는 강의 총합
  total = 0
  # count: 블루레이 개수
  count = 0
  for x in array:
    if total + x <= mid:
      total += x
    else:
      count += 1
      total = x
  if total:
    count += 1

  # 블루레이의 개수가 많으면 블루레이 크기를 늘림
  if count > m:
    start = mid + 1    
  # 블루레이 개수가 적으면 블루레이 크기를 줄임
  else:
    result = min(mid, result)
    end = mid - 1

print(result)