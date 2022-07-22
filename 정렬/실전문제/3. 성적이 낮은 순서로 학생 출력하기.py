n = int(input())

data = []
for i in range(n):
  a = list(input().split())
  data.append([a[0], int(a[1])])

data = sorted(data, key = lambda x: x[1])

for i in range(n):
  print(data[i][0])