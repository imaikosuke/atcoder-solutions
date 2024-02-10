a,b,c,d = map(int, input().split())

if a > c:
  print('Aoki')
elif c > a:
  print('Takahashi')
elif d >= b:
  print('Takahashi')
else:
  print('Aoki')