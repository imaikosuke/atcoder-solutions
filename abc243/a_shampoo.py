v,a,b,c = map(int, input().split())
sum = a + b + c
v %= sum
if v < a:
  print('F')
elif v < a + b:
  print('M')
else:
  print('T')