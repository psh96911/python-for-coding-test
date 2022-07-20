n = int(input())

count = 0
result = []
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  global count
  
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return False

  if graph[x][y] == 1:
    count +=1
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

  return False

for i in range(n):
  for j in range(n):
    if dfs(i,j):
      result.append(count)
      count = 0

result.sort()

print(len(result))
for i in range(len(result)):
  print(result[i])