import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()

left = 0
right = n-1

answer = abs(array[left] + array[right])
final = [array[left], array[right]]

while left < right:
    a = array[left]
    b = array[right]
    sum = a + b
  
    if abs(sum) < answer:
        answer = abs(sum)
        final = [a, b]
        if answer == 0:
          break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])