def solution(k, tangerine):
    dic = {}
    for t in tangerine :
        if t in dic:
            dic[t] += 1
        else : dic[t] = 1
    
    l = sorted(list(dic.values()),reverse=True)
    type_idx = 0
    cnt = 0
    for t in l :
        type_idx += 1
        cnt += t
        if(cnt >= k):
            print(type_idx)
            return type_idx
        