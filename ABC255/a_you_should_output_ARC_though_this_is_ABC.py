r, c = map(int, input().split())
a = [[0]*4 for _ in range(4)]

for i in range(1, 3):
    for j in range(1, 3):
        a[i][j] = int(input())
print(a[r][c])
