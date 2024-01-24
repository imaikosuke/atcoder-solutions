#---解答例１---#
n = int(input())
n = min(n,5)
if pow(2,n) > n*n:
  print('Yes')
else:
  print('No')

#---解答例２---#
n = int(input())
if n == 1 or n >= 5:
  print('Yes')
else:
  print('No')

#---間違った回答---#
# n = int(input())
# if 2**n > n**2:
#   print('Yes')
# else:
#   print('No')