n = int(input())
scores = list(map(int,input().split()))
mx = max(scores)
sum = 0
for i in scores :
    sum += i/mx*100
print(sum/n)