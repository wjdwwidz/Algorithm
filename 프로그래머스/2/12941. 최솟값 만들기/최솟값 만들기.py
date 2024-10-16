def solution(A,B):
    answer = 0
    sum = 0 
    A.sort(), B.sort(reverse=True)
    for a,b in zip (A,B): 
        sum +=  a*b
    return sum