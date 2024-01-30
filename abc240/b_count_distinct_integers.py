n = int(input())
array = [0]*n

index = 0
for num in map(int,input().split()):
  array[index] = num
  index += 1

print(len(set(array)))

# AtCoder公式解説による実装例
# n = int(input())
# print(len(set(map(int, input()split()))))