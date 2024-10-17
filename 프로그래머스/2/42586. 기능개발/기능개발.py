def solution(progresses, speeds):
    # 1. 작업 완료되는 일수들 계산하여 list 
    dues = []
    answer = []
    for p, s in zip(progresses, speeds):
        i = 0
        while(p<100):
            p +=s
            i +=1
        dues.append(i)

    # 2. idx로 반복문 돌리는데,val(idx)가 = d보다 작은 것 까지 sum ++
    first = dues[0]
    sum = 0
    for d in dues :
        #만약 뒤에 처리할 수 있는 게 있으면 거기까지 sum에 더함 
        if first >= d : sum +=1
        else : #처리할 수 있는 게 없으면 d를 새로운 처음으로 설정, 여태까지 모은 sum을 append, sum 1개로 초기화 
            first = d
            answer.append(sum)
            sum = 1
    # 3. sum ++ 를 기록 (new_list에 담기)
    answer.append(sum)
    return answer
