n = int(input())
h = list(map(int,input().split()))
ans = 0
while(ans+1 < n and h[ans] < h[ans+1]):
    ans += 1
print(h[ans])