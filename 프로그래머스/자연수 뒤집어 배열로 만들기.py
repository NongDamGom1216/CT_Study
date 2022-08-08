# 1단계

def solution(n):
    answer = []
    
    num = list(str(n))
    num.reverse()
    
    return list(map(int, num))