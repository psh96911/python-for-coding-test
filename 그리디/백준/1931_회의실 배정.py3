n = int(input())

time=[]
for i in range(n):
  a, b = list(map(int, input().split()))
  time.append([a,b])

time.sort(key = lambda x:(x[1], x[0]))

count = 1
end_time = time[0][1]
for i in range(n-1):
  if end_time > time[i+1][0]:
    continue
  else:
    count += 1
    end_time = time[i+1][1]
  
print(count)
