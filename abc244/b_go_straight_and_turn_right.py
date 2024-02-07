n = int(input())
t = list(input())
x = 0
y = 0
r = 0
for index in range(n):
  if t[index] == 'R':
    r += 1
  elif r % 4 == 0:
    x += 1
  elif r % 4 == 1:
    y -= 1
  elif r % 4 == 2:
    x -= 1
  else:
    y += 1
print(f"{x} {y}")