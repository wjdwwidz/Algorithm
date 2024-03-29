def solution(array, commands):
    answer = []
    for command in commands:
        start, end, cut = command
        arr = array[start-1:end]
        arr.sort()
        answer.append(arr[cut-1])
        # print(answer)
    return answer
