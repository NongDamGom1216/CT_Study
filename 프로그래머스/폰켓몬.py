# 1단계

def solution(nums):
    answer = 0
    # set으로 중복을 제거하는 것이 포인트
    
    set_list = set(nums)
    
    if len(nums) // 2 > len(set_list):
        return len(set_list)
    else:
        return len(nums) // 2
    
    
    
    
    return answer