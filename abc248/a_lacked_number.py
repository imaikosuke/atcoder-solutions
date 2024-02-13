s = list(input())
s = sorted(s)
index = 0
while str(index) == s[index]:
  index += 1
  if index == 9:
    break
print(str(index))