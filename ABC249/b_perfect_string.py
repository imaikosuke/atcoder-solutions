s = input()
if len(s) != len(set(s)): # 重複がある場合
    print("No")
    exit()
if s.islower() or s.isupper(): # すべて小文字か大文字の場合
    print("No")
    exit()
print("Yes")