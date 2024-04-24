def solution(s) : 
    answer = 0
    n = len(s)
    for i in range(n) :
        opens = []
        for j in range(n) : 
            c = s[(i+j)%n]
            if c == "()" or c =="[" or c =="{" : 
                opens.append(c)
            else :
                if not opens : 
                    break

            #닫힌 괄호는 스택의 top과 짝이 맞는지 비교 
            if c == "(" and opens[-1] == "(" :
                opens.pop()
            elif c == "]" and opens[-1] == "[" :
                opens.pop()
            elif c == "}" and opens[-1] == "{" :
                opens.pop()
            else: break

        else :
            if not opens:
                answer += 1
    return answer

        

            