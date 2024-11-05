word1 = list(input())
word2 = list(input())

cnt = 0  # 카운트 초기화

for w in word2:
    if w in word1:
        word1.remove(w) 
    else:
        cnt += 1  

cnt += len(word1) 

print(cnt)


