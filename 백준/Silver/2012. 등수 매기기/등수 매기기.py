import sys

n = int(sys.stdin.readline())
ex_arr = [int(sys.stdin.readline()) for x in range(n)]

ex_arr.sort()

diff = 0

for i in range(len(ex_arr)) : 
    diff += abs(ex_arr[i] - (i+1))
print(diff)