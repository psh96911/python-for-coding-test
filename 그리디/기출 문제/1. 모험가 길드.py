n = int(input())
data = list(map(int, input().split()))


data.sort(reverse=True)

count = 0

while n > 0:
  a = data[0]
  n -= a
  count +=1
  data = data[a:]

print(count)


