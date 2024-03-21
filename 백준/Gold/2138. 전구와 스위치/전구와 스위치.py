import sys
input = sys.stdin.readline

n = int(input())
current = list(map(int, input().rstrip("\n")))
target = list(map(int, input().rstrip("\n")))

def switch(current, target):
    cnt = 0
    for i in range(1, n):
        if current[i - 1] != target[i - 1]:
            cnt += 1
            # 스위치를 누르는 작업
            for j in range(i - 1, i + 2):
                if 0 <= j < n:
                    current[j] = 1 - current[j]
    
    # 모든 전구 상태가 목표와 일치하는지 확인
    if current == target:
        return cnt
    else:
        return float('inf')  # 불가능한 경우

# 첫 번째 스위치를 누르지 않은 경우
answer = switch(current[:], target[:])

# 첫 번째 스위치를 누른 경우
current[0] = 1 - current[0]
current[1] = 1 - current[1]
answer = min(answer, switch(current[:], target[:]) + 1)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
