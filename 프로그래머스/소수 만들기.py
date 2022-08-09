# 1단계
# 풀이 참조

from itertools import combinations

def prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num//2+1)):
            if num % i == 0:
                return False
        return True
    

def solution(nums):
    answer = 0
    
    temp = list(combinations(nums,3))
    # [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
    
    for i in temp:
        if prime(sum(i)):
            answer += 1

    return answer