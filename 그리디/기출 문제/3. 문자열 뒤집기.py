s = input()

count0 = 0  #모두 0으로 만드는 횟수
count1 = 0  #모두 1로 만드는 횟수

if int(s[0])==0:
  count1 +=1
elif int(s[0])==1:
  count0 += 1


for i in range(len(s)-1):
  if int(s[i]) != int(s[i+1]):
    if int(s[i+1]) == 1:
      count0 += 1
    else: 
      count1 += 1

print(min(count0, count1))
