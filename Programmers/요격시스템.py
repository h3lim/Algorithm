def solution(targets):
    ans = []
    targets.sort(key=lambda i: i[0])
    ans.append(targets[0])
    for start, end in targets:
        lastE = ans[-1][1]

        if lastE > start:
            ans[-1][1] = min(lastE, end)
        else:
            ans.append([start, end])

    return len(ans)