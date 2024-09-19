day =0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

x,y = map(int,input().split())
#days[x] 까지의 value 들만 더함
for i in range(x-1):
    day += arrList[i]

day = (day+ y)%7
print(weekList[day])