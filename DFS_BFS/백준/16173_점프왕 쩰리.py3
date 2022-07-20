from collections import deque

n = int(input())

graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

visited = [[0]*n for _ in range(n)]

# 아래, 오른쪽

dx = [0,1]
dy = [1,0]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, n - 1):
            return True
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==0:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return False

print("HaruHaru" if bfs(0,0) else "Hing")