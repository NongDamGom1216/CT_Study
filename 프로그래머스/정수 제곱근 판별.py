# 1단계

def solution(n):
    answer = 0
    
    num = n ** 0.5 # 0.5 제곱을 하는 방법
    
    if num == int(num):
        num += 1
        return num ** 2
    else:
        return -1
