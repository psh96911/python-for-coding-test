import sys

n = int(sys.stdin.readline())

result = []
for i in range(n):
  x = int(sys.stdin.readline())
  if x==0:
    result = result[:-1]
  else:
    result.append(x)

print(sum(result))