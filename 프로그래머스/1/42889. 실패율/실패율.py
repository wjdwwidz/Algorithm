def solution(N, stages):
    failureRates = []
    for j in range(1, N + 1):
        head, tail = 0, 0
        for stage in stages:
            if stage >= j:
                tail += 1
            if stage == j:
                head += 1
        failureRates.append(head / tail if tail != 0 else 0)
    return failureRates

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))