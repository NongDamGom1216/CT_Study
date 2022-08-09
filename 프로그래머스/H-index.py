# 2단계

def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse = True)
    # 6 5 3 1 0
    
    for i , citation in enumerate(citations):
        if i >= citation:
            return i
    # i : citation
    # 0 : 6
    # 1 : 5
    # 2 : 3
    # 3 : 1
    # 4 : 0
    
    return len(citations)