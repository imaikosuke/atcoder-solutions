N, W = map(int, input().split())
A = list(map(int, input().split()))

possible_sums = set()

for i in range(N):
    # 単体でW以下の場合
    if A[i] <= W:
        possible_sums.add(A[i])
    for j in range(i + 1, N):
        # 2つの要素の和がW以下の場合
        if A[i] + A[j] <= W:
            possible_sums.add(A[i] + A[j])
        for k in range(j + 1, N):
            # 3つの要素の和がW以下の場合
            sum_ijk = A[i] + A[j] + A[k]
            if sum_ijk <= W:
                possible_sums.add(sum_ijk)

print(len(possible_sums))
