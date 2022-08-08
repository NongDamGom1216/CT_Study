# 1단계

#유클리드 호제법 이용

def solution(n, m):
    answer = []
    
    # 최대공약수
    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
        
    # 최소공배수    
    for i in range(max(n,m), n*m+1):
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break
    
    return answer