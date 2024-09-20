'''
1. n-1개의 원판을 1번에서 2번 막대로 옮긴다
2. n번째 원판을 3번 막대로 옮긴다
3. n-1개의 원판을 2번에서 3번 막대로 옮긴다
'''

def hanoi(n, start, end) : #n개 , 시작막대, 도착막대
    if(n == 1) : 
        print(start, end)
        return
    
    hanoi(n-1, start, 6-start-end) 
    #start,end 는 알지만 나머지 막대의 번호를 알 수 없으므로 (1+2+3)에서 start와 end를 뺀다
    print(start, end)
    hanoi(n-1, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi(n,1,3)