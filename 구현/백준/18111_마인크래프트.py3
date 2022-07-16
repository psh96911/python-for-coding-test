import sys

n, m, b = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = sys.maxsize

# 0층부터 256층까지 반복
for height in range(257):
  max_h = 0
  min_h = 0
  for i in range(n):
    for j in range(m):
      # 블록이 층수보다 더 크면
      if data[i][j] > height:
        max_h += (data[i][j] - height)
      # 블록이 층수보다 더 작으면
      else:
        min_h += (height - data[i][j])

  # 원래있는 것 + 블록 뺀 것  vs   블록 더한 것
  inventory = max_h + b
  if inventory < min_h:
    continue
  time = 2 * max_h + min_h
  if time <= ans:
    ans = 2 * max_h + min_h
    h = height

print(ans, h)