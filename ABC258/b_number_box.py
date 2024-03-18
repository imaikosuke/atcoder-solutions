n = int(input())
a = []

for _ in range(n):
    row = input()
    a.append([int(c) for c in row])

p = [1, 1, 1, 0, 0, -1, -1, -1]
q = [1, 0, -1, 1, -1, 1, 0, -1]

ans = 0

for i in range(n):
    for j in range(n):
        for k in range(8):
            now = 0
            x, y = i, j
            # n回連結
            for _ in range(n):
                now = now * 10 + a[x][y]
                x, y = (x + p[k]) % n, (y + q[k]) % n
            ans = max(ans, now)

print(ans)
