def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]  # 수정: 리스트 슬라이싱에서 end 인덱스 수정
        cut = commands[i][2] - 1
        arr = sorted(array[start:end])  # 수정: sorted() 함수 사용
        answer.append(arr[cut])

    return answer