n, k = map(int, input().split())

count = 0

while n>=k:
  if n%k!=0:
    n -= 1
    count += 1
  else:
    n //= k
    count += 1

count += (n-1)

print(count)
