n = int(input())
arr = [int(x) for x in (input().split())]

arr.sort()
time = 0
for i in range(n):
    time += arr[i] * (n-i)
print(time)