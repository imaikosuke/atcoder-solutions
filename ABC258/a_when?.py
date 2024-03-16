k = int(input())
h = k // 60
h += 21
m = k % 60

if 23 < h:
    h -= 24

print(str(h) + ":" + str(m))