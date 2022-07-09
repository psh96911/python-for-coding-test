start = str(input())

result = 0



if start[0] == '-':
  data = start[1:].split('-')
  result -= sum(map(int, data[0].split('+')))
else: 
  data = start.split('-')
  result += sum(map(int, data[0].split('+')))


for x in range(1, len(data)):
  result -= sum(map(int, data[x].split('+')))

print(result)
  