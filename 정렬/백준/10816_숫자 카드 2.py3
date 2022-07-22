import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dic1 = {}

for i in a:
  if i in dic1:
    dic1[i] += 1
  else:
    dic1[i] = 1


m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))


for j in b:
  if j in dic1:
    print(dic1[j], end = " ")
  else:
    print(0, end=" ")