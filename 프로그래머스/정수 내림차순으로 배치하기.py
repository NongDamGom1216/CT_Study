#  1단계

def solution(n):
    answer = 0
    
    num = list(str(n))
    num = sorted(num, reverse = True)
    
    return int(''.join(num))