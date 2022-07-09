n, l = map(int, input().split())

data= list(map(int, input().split()))

data.sort()

start = data[0]-0.5
count = 1

for i in range(1, n):
  if start + l >= data[i]+0.5:
    continue
  else:
    count += 1
    start = data[i] - 0.5

print(count)
  
