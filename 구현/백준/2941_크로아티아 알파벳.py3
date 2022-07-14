data = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for cro in croatia:
  if cro in data:
    data = data.replace(cro, '_')
    
print(len(data))