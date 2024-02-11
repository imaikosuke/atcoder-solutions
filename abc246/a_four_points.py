x = [0]*3
y = [0]*3

for i in range(2):
  x[i],y[i] = map(int,input().split())

# x座標を計算
if x[0] == x[1]:
    x_ans = x[2]
elif x[1] == x[2]:
    x_ans = x[0]
elif x[2] == x[0]:
    x_ans = x[1]

# y座標を計算
if y[0] == y[1]:
    y_ans = y[2]
elif y[1] == y[2]:
    y_ans = y[0]
elif y[2] == y[0]:
    y_ans = y[1]

# 結果を出力
print(x_ans, y_ans)