import math

n, k = map(int, input().split())
a = [int(input()) - 1 for _ in range(k)]

x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

# 最大距離を計算
res = 0
for i in range(n):
    cres = float('inf')
    for nx in a:
        # 現在の点から選択された点までの距離を計算し、現在の最小値と比較
        cres = min(cres, (x[i] - x[nx])**2 + (y[i] - y[nx])**2)
    # 全点を通じた最大の最小距離を更新
    res = max(res, cres)

# 結果の平方根を計算し、12桁の小数点以下で出力
print(f"{math.sqrt(res):.12f}")
