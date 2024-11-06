
def solution(n):
    target =list(bin(n)[2:]).count("1")
    cnt = 0
            
    next = n
    while (target != cnt) :
        next += 1
        cnt = list(bin(next)[2:]).count("1")
        if(target==cnt) :
            return next