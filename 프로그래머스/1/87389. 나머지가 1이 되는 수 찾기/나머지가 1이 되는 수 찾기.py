def solution(n):
    answer = 0
    min = n
    for i in range(2, n):
        if n % i == 1 and i < min:
            min = i
    answer = min
    return answer