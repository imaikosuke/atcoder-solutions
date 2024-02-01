from collections import Counter
input()
a = Counter(input().split())
b = Counter(input().split())
print('No' if b - a else 'Yes')