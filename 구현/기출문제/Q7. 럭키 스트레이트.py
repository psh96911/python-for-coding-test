n = input()

m = len(n)//2

a = str(n)[:m]
b = str(n)[m:]

a_sum = sum(list(map(int,a)))
b_sum = sum(list(map(int,b)))

if a_sum == b_sum:
  print('LUCKY')
else:
  print('READY')
