n = int(input())
row = [1]

for _ in range(n):
    print(' '.join(map(str, row)))
    row = [x + y for x, y in zip([0] + row, row + [0])]