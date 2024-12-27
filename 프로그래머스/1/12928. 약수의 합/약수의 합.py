def solution(n):
    i = 1
    cnt = 0
    while i <= n :
        if (n%i == 0) :
            cnt += i 
        i += 1
    
    return cnt