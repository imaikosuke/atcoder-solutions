a,b,c,x = map(int, input().split())
if a >= x:
  print(1)
elif x > b:
  print(0)
else:
  print(c / (b-a))