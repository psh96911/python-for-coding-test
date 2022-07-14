data = [i for i in range(1,10001)]

for i in range(1, 10001):
  a = str(i)
  num = i + sum(list(map(int, a)))

  if num in data:
    data.remove(num)

for i in data:
  print(i)
