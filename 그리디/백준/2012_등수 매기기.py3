import sys
n = int(sys.stdin.readline().rstrip())
data = sorted(int(sys.stdin.readline().rstrip()) for i in range(n))

data_real =list(range(1,n+1))

diff = [a - b for a, b in zip(data, data_real)]

result = sum( map(abs, diff) )
print(result)