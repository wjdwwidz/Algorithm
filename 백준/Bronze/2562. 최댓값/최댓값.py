mx = 0
mx_index = 0
for i in range(9):
    n = int(input())

    if (mx<n) : 

        mx = n
        mx_index = i
    
print(mx, mx_index+1)
    