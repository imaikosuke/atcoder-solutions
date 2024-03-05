h, w = map(int, input().split())
s = [input() for _ in range(h)]
points = []

for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            points.append((i, j))

a, b = points[0]
c, d = points[1]
print(abs(a - c) + abs(b - d))