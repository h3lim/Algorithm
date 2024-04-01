def solution(clothes):
    ans = 1
    dic = dict()
    l = []
    for cloth, category in clothes:
        if category not in dic.keys():
            dic[category] = [cloth]
        else:
            dic[category].append(cloth)

    for _, i in dic.items():
        ans *= (len(i) + 1)

    return ans - 1