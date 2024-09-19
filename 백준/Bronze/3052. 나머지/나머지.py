arr =[]
for i in range(10):
        n = int(input())
        arr.append(n%42)


answer = len(set(arr))
print(answer)

