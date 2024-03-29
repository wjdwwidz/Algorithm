def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]  
        cut = commands[i][2] - 1
        arr = sorted(array[start:end])
        answer.append(arr[cut])

    return answer
