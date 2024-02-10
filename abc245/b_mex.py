n = int(input())
a = [0]*n

index = 0
for i in map(int, input().split()):
  a[index] = i
  index += 1

a_set = set(a)
for i in range(2001):
  if i not in a_set:
    print(i)
    break