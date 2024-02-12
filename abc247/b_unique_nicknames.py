def can_use_nickname(u, idx, N, ST):
    # 人idxがuをあだ名に使えるか？
    return all(u not in ST[i] for i in range(N) if i != idx)

def judge():
    N = int(input())
    ST = [input().split() for _ in range(N)]
    return all(can_use_nickname(si, i, N, ST) or can_use_nickname(ti, i, N, ST) for i, (si, ti) in enumerate(ST))

print("Yes" if judge() else "No")
