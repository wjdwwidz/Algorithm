arr = list(range(1,31))
for i in range(28) :
    n = int(input())
    arr.remove(n)

print(sorted(arr)[0])
print(sorted(arr)[1])
