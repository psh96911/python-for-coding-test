n = int(input())

data = []
for i in range(n):
  a = int(input())
  data.append(a)

data.sort()

result = []
for i in range(n):
  result.append((i+1)*data[n-i-1])

print(max(result))