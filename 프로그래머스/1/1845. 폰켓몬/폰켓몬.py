def solution(nums):
    print(set(nums))
    if len(set(nums)) <= (len(nums)/2):
        answer = len(set(nums))
    else : answer = (len(nums)/2)
    return int(answer)