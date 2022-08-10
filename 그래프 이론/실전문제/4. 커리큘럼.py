from collections import deque
import copy
import sys
input = sys.stdin.readline

v = int(input())

# 진입차수
indegree = [0] * (v+1)

# 간선 정보
graph = [[] for i in range(v+1)]

# 각 강의 시간
time = [0] * (v+1)

for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0]
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

def topology_sort():
  result = copy.deepcopy(time)
  q = deque()

  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, v+1):
    print(result[i])

topology_sort()