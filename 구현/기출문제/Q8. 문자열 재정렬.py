data = input()
data = sorted(data)

result_alpha = []
result_num = 0

for i in data:
  if i.isalpha():
    result_alpha.append(i)
  else:
    result_num += int(i)

result_alpha.append(str(result_num))
result = "".join(result_alpha)
print(result)



