s = input()
if len(s) != len(set(s)):
    print("No")
    exit()
if s.islower() or s.isupper():
    print("No")
    exit()
print("Yes")