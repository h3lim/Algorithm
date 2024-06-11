import math


def solution(k, d):
    ans = 0

    # 피타고라스 정리 이용하여 maximum Y값 계산 후 그 값을 k로 나누고 + 1
    for x in range(0, d + 1, k):
        maxY = math.sqrt((d ** 2 - x ** 2))
        ans += (maxY // k) + 1

    return ans