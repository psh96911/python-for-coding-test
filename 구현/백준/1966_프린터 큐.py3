x = int(input())

for i in range(x):
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  data1 = list(enumerate(data))
  count = 0

  while True:
    if data1[0][1] == max(data):
      a = data1.pop(0)
      data.pop(0)
      count += 1
      
      if a[0] == m:
        print(count)
        break
    
    else:
      b = data1.pop(0)
      data.pop(0)
      data1.append(b)
      data.append(b[1])
      
