N, K = map(int, input().split())
numbers = list(map(int, input().split()))
counter = [0]* (max(numbers)+1)

start = 0
end = 0
cnt = 0

while end < N : 
    if counter[numbers[end]] < K :
        counter[numbers[end]] += 1
        end += 1
    else :
        counter[numbers[start]] -= 1
        start += 1
    cnt = max(end-start, cnt)

print(cnt)