n, m, k = map(int, input().split())
data= list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result1 = m//(k+1) * (k*first+second)
result2 = m%(k+1) * first 
result = result1 + result2

print(result)