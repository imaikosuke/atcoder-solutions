N = int(input())
A = list(map(int, input().split()))
P = 0
field = [False] * 4

for x in A:
  next_field = [0] * 4
  field[0] = True
  for i in range(4):
    if field[i] == True:
      if i + x >= 4:
        P += 1
      else:
        next_field[i + x] = True
  field = next_field

print(P)