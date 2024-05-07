import sys

input_data = input().split(' ')
length = int(input_data[0])
jump = int(input_data[1])

arr = list(range(1, length + 1))
currentIndex = 0
survivors = length
answer = []

while survivors >= 1:
    currentIndex = (currentIndex + jump - 1) % survivors
    answer.append(arr[currentIndex])
    del arr[currentIndex]
    survivors -= 1

print(f"<{', '.join(map(str, answer))}>")
