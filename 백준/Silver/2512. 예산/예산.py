n = int(input()) 
arr = list(map(int, input().split()))  
m = int(input()) 

arr.sort()

temp = 0
for i in range(n):
    temp += arr[i]

    # 누적합이 총예산을 넘으면 stop!
    if temp > m:
        cur = i  # 현재 인덱스 저장

        # cur 하나씩 줄이면서 상한액 구하기
        while cur >= 0:
            # 0~(cur-1)까지의 합 구하기
            psum = sum(arr[:cur])

            # 임시 상한액 = (m - 누적합) / 남은 개수
            result = (m - psum) // (n - cur)

            # 임시 상한액 >= 바로 앞의 금액 (종료 조건 1)
            if result >= arr[cur - 1]:
                # 상한액 출력
                print(result)
                exit(0)
            else:
                cur -= 1

        # cur가 0까지 이동한 경우 (종료 조건 2)
        print(m // n)
        exit(0)

# 다 더해도 m을 넘지 않으면 마지막 원소 자체가 상한액 (종료 조건 3)
print(arr[n - 1])
