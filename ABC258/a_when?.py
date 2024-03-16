k = int(input())
h = 21
if 60 <= k:
    h = 22
m = k % 60
print(f'{h}:{m:02}')