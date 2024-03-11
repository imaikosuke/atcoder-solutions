N, X = map(int, input().split())
ascii_num = ord('A') + (X - 1) // N
print(chr(ascii_num))