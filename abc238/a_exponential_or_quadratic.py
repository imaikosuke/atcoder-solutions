n = int(input())
n = min(n,10)
ans = 'No'
if pow(2,n) > n*n:
    ans = 'Yes'
print(ans)

#---自分の間違った回答---#
# n = int(input())
# if 2**n > n**2:
#   print('Yes')
# else:
#   print('No')