n = int(input())
cards = [0]*(n)

for i in map(int, input().split()):
  cards[i-1] += 1

for i in range(n):
  if cards[i] == 3:
    print(i+1)