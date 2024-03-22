import sys 
input = sys.stdin.readline
N,M,L,K = map(int, input().split())

stars = []
for i in range (K):
    x,y = map(int,input().split())
    stars.append([x,y])

def count (x,y) :
    cnt = 0
    for i in range (K) :
        # x,y 좌표가 K*K 범위 안에 있는지 확인
        if (x<= (stars[i][0]) <= x+L) and (y<= stars[i][1] <= y+L) :
            cnt +=1
    return cnt

answer =0
# K*K 범위 안에 있는지 확인
for i in range (K):
    for j in range (K):
        answer = max(answer, count(stars[i][0],stars[j][1]))

print (K-answer)