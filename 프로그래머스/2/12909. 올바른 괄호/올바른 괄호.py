def solution(s) :
    stack = []
    for i in range (len(s)) : 
        if s[i] == "(" : 
            stack.append(s[i])
        if s[i] == ")" : 
            if not stack: 
                return False
            else : 
                stack.pop()

    return len(stack) == 0
