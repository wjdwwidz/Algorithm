def solution(arr):
    answer = []
    for i in arr :
        if len(answer) == 0 :
            answer.append(i)
        if i != answer[-1] :  
            answer.append(i)
    return answer
