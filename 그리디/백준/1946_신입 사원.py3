import sys

n = int(input())

for i in range(n):
  m = int(input())
  score = []
  for j in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    score.append([a,b])
  
  score.sort(key = lambda x: x[0])

  score_min = score[0][1]
  count = 1
  
  for x in range(m-1):
    if score_min > score[x+1][1]:
      count += 1
      score_min= [score_min]
      score_min.append(score[x+1][1])
      score_min = min(score_min)

  print(count)
