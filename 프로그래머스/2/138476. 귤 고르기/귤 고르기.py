from collections import Counter

def solution(k, tangerine):
   l = sorted(Counter(tangerine).values(),reverse=True)
   cnt = 0
   for i,v in enumerate(l) :
    cnt += v
    if (cnt >= k): return i+1
