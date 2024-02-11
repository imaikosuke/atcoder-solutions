x, y = map(int, input().split())

# 原点からの距離の二乗を計算
d2 = x**2 + y**2

# 距離を計算
d = d2**0.5

# 正規化された座標を計算
dx = x / d
dy = y / d

print(dx, dy)
