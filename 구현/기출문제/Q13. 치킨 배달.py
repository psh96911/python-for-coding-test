from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
  data = list(map(int, input().split()))
  for c in range(n):
    if data[c] == 1:
      house.append([r,c])
    elif data[c] == 2:
      chicken.append([r,c])

# 모든 조합
candidates = list(combinations(chicken, m))

def distance(candidate):
  result = 0
  for hx, hy in house:
    temp = 1e9
    for cx, cy in candidate:
      # 치킨거리(집과 가장 가까운 치킨집 거리)
      temp = min(temp, abs(hx-cx) + abs(hy-cy))

    # 도시의 치킨 거리(모든 집의 치킨 거리의 합)
    result += temp
  return(result)

result = 1e9

for candidate in candidates:
  result = min(result, distance(candidate))

print(result)

    



  