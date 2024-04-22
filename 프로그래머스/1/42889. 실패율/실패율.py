def solution(N,stages) : 
    #스테이지 별 도전자 수 구하기
    challanger = [0] * (N + 2)
    for stage in stages : 
        challanger[stage] += 1
    
    #스테이지별 실패한 사용자 계산 
    fails = {}
    total = len(stages)

    #각 스테이지를 순회하며 실패율 계산
    for i in range(1, N + 1) :
        if challanger[i] == 0 : #도전한 사람이 없는 경우 실패율 = 0
            fails[i] = 0
        else :
            fails[i] = challanger[i] / total #실패율 구함
            total -= challanger[i] #다음 스테이지 실패율을 구하기 위해 현재 스테이지의 인원을 뺌

    #실패율이 높은 스테이지부터 내림차순으로 정렬
    result = sorted(fails, key=lambda x : fails[x], reverse = True)

    return result