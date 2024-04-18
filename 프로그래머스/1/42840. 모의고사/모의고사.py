def solution(answers):
    
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    scores =[0,0,0]
    cnt = 0
    
    #answers의 크기만큼 배열을 순회하면서 값이 같은지 count
    for i , answer in enumerate(answers) :
        for j ,pattern in enumerate(patterns) :
            if answer == pattern[i%len(pattern)] :
                scores[j] += 1

    max_score = max(scores)
    highest_scores = []

    for i, score in enumerate(scores) :
        if score == max_score:
            highest_scores.append(i+1)
    return highest_scores