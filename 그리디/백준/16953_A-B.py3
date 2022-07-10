a, b = map(int, input().split())

count = 1

while b != a:
  if a > b or (b%10 != 1 and b%2 != 0):
    count = -1
    break
  elif b%10 == 1:
    b = (b-1)/10
    count += 1
  elif b%2 == 0:
    b /= 2
    count += 1

print(count)