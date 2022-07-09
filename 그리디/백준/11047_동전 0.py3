n, k = map(int, input().split())

coin=[]
for i in range(n):
  coin_input = int(input())
  coin.append(coin_input)


coin.sort(reverse=True)

count = 0

for i in range(n):
  if k//coin[i] >= 1:
    count += k//coin[i]
    k -= k//coin[i] * coin[i]

print(count)