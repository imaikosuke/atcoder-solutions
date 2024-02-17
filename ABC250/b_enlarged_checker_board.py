n, a, b = map(int, input().split())
grid = []

for _ in range(5):
    for row in range(a):
        grid.append(("." * b + "#" * b) * 5)
    for row in range(a):
        grid.append(("#" * b + "." * b) * 5)


for row in range(a * n):
    print(grid[row][:b * n])
