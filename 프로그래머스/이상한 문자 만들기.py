# 1단계

def solution(s):
    answer = ''
    
    list = s.split(' ')
    
    for i in list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    
    return answer[:-1]
        