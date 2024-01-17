from math import sqrt
n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())
ans = 0
for i in range(n):
    for j in range(i+1, n):
        x_len = x[i] - x[j]
        y_len = y[i] - y[j]
        ans = max(ans, sqrt(x_len*x_len + y_len*y_len))
print(ans)