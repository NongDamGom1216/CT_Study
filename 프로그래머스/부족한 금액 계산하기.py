# 1단계

def solution(price, money, count):
    total = 0
    
    for i in range(1, count+1):
        total += i * price

    if total > money:
        answer = total - money
    else:
        return 0
    
    return answer