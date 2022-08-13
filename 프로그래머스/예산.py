# 1단계
# 스킬체크 1

def solution(d, budget):
    d.sort()
    
    while budget < sum(d):
        d.pop()
    
    return len(d)