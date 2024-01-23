n = int(input())

max = pow(2, 31)
min = -max

if (min <= n and n < max):
  print('Yes')
else:
  print('No')