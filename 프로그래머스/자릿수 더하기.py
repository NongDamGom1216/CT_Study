# 1단계

def solution(n):
    answer = 0

    num = list(map(int, str(n)))
    # [1,2,3]
    # num = list(str(n)) 은 ["1", "2", "3"]
    
    for i in range(len(num)):
        answer += num[i]
    

    return answer