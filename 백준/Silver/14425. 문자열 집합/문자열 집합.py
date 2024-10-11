import sys 
input = sys.stdin.readline

n,m = map(int, input().split())
d = {}
cnt = 0 
for i in range(n):
    s = input().rstrip()
    d[s] = 1

for j in range(m) :
    t = input().rstrip()
    if t in d :
        cnt +=1 

print(cnt)