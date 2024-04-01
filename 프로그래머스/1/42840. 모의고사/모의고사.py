def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_a = count_b = count_c = 0
    
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            count_a += 1
        if b[i % len(b)] == answers[i]:
            count_b += 1
        if c[i % len(c)] == answers[i]:
            count_c += 1
            
    max_count = max(count_a, count_b, count_c)
    
    if max_count == count_a:
        answer.append(1)
    if max_count == count_b:
        answer.append(2)
    if max_count == count_c:
        answer.append(3)
        
    return answer

