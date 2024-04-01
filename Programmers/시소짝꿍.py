from collections import Counter
def solution(weights):
    ans = 0
    cnt = Counter(weights)

    for k, v in cnt.items():
        if v >= 2:
            ans += v * (v - 1) // 2

    weights = set(weights)

    for i in weights:
        if i * 2 / 3 in weights:
            ans += cnt[i * 2 / 3] * cnt[i]
        if i * 2 / 4 in weights:
            ans += cnt[i * 2 / 4] * cnt[i]
        if i * 3 / 4 in weights:
            ans += cnt[i * 3 / 4] * cnt[i]

    return ans