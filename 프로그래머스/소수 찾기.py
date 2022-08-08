# 1단계

def solution(n):
    answer = 0
    
    list=set(range(2,n+1)) # 2부터 n+1까지의 집합

    
    for i in range(2, n+1):
        if i in list:
            # 참고
            list-=set(range(2*i,n+1,i)) # i의 배수는 num 집합에서 제외
            
    answer = len(list)
    
    return answer