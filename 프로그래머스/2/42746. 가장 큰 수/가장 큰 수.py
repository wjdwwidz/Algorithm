def compare(x):
    return x * 3

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=compare, reverse=True)
    return str(int(''.join(numbers)))
