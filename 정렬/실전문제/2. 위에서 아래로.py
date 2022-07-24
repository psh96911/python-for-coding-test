n = int(input())

data = []
for i in range(n):
  a = int(input())
  data.append(a)

data.sort(reverse=True)

for i in range(n):
  print(data[i], end = " ")
