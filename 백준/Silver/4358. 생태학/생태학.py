import sys
names_dic = {}
total_len = 0

while 1 :
    line = sys.stdin.readline().strip()
    if line == "" :
        break
    
    if line in names_dic : 
        names_dic[line] +=1
    else : names_dic[line] = 1

total_len = sum(names_dic.values())

    #비율 계산 및 사전순 정렬 
for key,val in names_dic.items() : 
    names_dic[key] = (val/total_len)*100

sorted_dic = dict(sorted(names_dic.items()))
for names in sorted_dic : print(f"{names} {sorted_dic[names]:.4f}")
