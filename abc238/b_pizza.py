n = int(input())
angles = list(map(int, input().split()))

flags = [False] * 360
flags[0] = True
position = 0

# 角度リストを使ってピザを切る
for angle in angles:
    position = (position + angle) % 360
    flags[position] = True

max_angle = 0
cur = 0

# 最大のピザスライスの角度を計算
for i in range(361):
    if flags[i % 360]:
        max_angle = max(max_angle, cur)
        cur = 0
    cur += 1

print(max_angle)
