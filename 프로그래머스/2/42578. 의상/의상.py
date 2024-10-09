def solution(clothes):
    dic = {} #{모자 : 개수}
    for cloth in clothes :
        if cloth[1] in dic :
            dic[cloth[1]] += 1
        else : dic[cloth[1]] = 1
    # print(dic)

    answer = 1
     
    for d in dic : 
        dic[d] += 1
        answer *= dic[d]
            
    return answer -1