from collections import deque
n,k = map(int, input().split())

def sol(n,k) :
    answer = []
    idx = 0
    people = list(range(1,n+1))

    while people :
        #인덱스 기준으로 계산하므로 k도 -1 필요
        idx = (idx + k - 1) % len(people)
        answer.append(people.pop(idx))

    print ('<'+str(answer)[1:-1]+'>')

sol(n,k)