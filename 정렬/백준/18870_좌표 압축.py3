import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

unique_data = sorted(set(data)) 


dic = {unique_data[i] : i for i in range(len(unique_data))}

for i in data:
  print(dic[i], end=" ")