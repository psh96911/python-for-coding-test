import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

a = len(array)//2
if len(array) % 2 == 0:
  print(array[a-1])
else:
  print(array[a])