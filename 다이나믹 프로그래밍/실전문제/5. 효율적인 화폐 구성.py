n, m = map(int, input().split())
array = []
for i in range(n):
  a = int(input())
  array.append(a)

d = [10001] * (m+1)
d[0] = 0

# i: 화폐 단위 / j: 금액
for i in array:
  for j in range(i,m+1):
    if d[j-i] != 10001:
      d[j] = min(d[j], d[j-i]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
