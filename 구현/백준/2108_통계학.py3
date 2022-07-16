from collections import Counter
import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
  a = int(sys.stdin.readline())
  data.append(a)

data.sort()

count = Counter(data)
cnt = count.most_common()
cnt_max = []

for i in range(len(cnt)):
  if cnt[i][1] == cnt[0][1]:
    cnt_max.append(cnt[i])

if len(cnt_max) == 1:
  mode = cnt_max[0][0]
else:
  mode = cnt_max[1][0]

print(int(round(sum(data)/len(data), 0))) # 평균
print(data[len(data)//2]) # 중앙값
print(mode) # 최빈값
print(max(data)-min(data)) # 범위