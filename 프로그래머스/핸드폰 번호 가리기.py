# 1단계

def solution(phone_number):
    answer = ''
    l = len(phone_number)
    
    for i in range(l-4):
        answer += '*'
    
    answer += phone_number[-4:]
    
    return answer