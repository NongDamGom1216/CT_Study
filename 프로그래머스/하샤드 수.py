# 1단계

def solution(x):
    answer = True
    
    arr = list(str(x))
    
    sum = 0
    
    for i in range(len(arr)):
        sum += int(arr[i])
        
    if x % sum == 0:
        return True
    else:
        return False
    