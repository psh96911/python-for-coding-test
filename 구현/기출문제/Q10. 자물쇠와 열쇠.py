n, m = map(int, input().split())

key = [[0]*m for _ in range(m)]
for i in range(m):
  key_input = list(map(int, input().split()))
  key[i] = key_input

lock = [[0]*n for _ in range(n)]
for i in range(n):
  lock_input = list(map(int, input().split()))
  lock[i] = lock_input

def create_graph(n, lock):
      graph = [[0] * (3*n) for _ in range(3*n)] #차원 3배 확장
      for i in range(n):
          for j in range(n):
              graph[i + n][j + n] = lock[i][j]
      return graph

def unlock(n, graph):
      for i in range(n, 2*n):
          for j in range(n, 2*n):
              if graph[i][j] != 1: # 자물쇠 부분이 모두 1인지 확인
                  return False
      return True

def rotate(m, key):
      nkey = [[0] * m for _ in range(m)]
      for i in range(m):
          for j in range(m):
              nkey[j][m - i - 1] = key[i][j] # 시계방향 90도 회전
      return nkey

def solution(key, lock):
      n, m = len(lock), len(key)
      graph = create_graph(n, lock)
      for _ in range(4):  # 90, 180, 270, 360
          key = rotate(m, key)
          for x in range(2*n):
              for y in range(2*n):
                  for i in range(m):
                      for j in range(m):
                          graph[x + i][y + j] += key[i][j]
 
                  if unlock(n, graph):
                      return True
 
                  for i in range(m):
                      for j in range(m):
                          graph[x + i][y + j] -= key[i][j]
 
      return False

print(solution(key, lock))

"""
main idea:
자물쇠 크기를 3배로 확장하여 생각
>> 자물쇠 영역을 벗어난 부분까지 고려하기위해서
>> 가운데 m x m이 전부 1이 될 때 unlock
"""