import math
def solution(progresses, speeds):
    ans = []
    tmp = []
    for i in range(len(progresses)):
        tmp.append(math.ceil((100 - progresses[i]) / speeds[i]))
    days = tmp[0]
    cnt = 1
    print(tmp)
    for i in range(1,len(tmp)):
        if days < tmp[i]:
            ans.append(cnt)
            days = tmp[i]
            cnt = 1
        else:
            cnt+= 1
    ans.append(cnt)
    return ans