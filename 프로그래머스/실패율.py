# 1단계

# 어려워서 답 보고 함

def solution(N, stages):
    answer = []
    player = len(stages) # 스테이지에 도달한 사람의 수
    dict = {}
    
    for i in range(1, N+1):
        count = 0 # 해당 스테이지를 클리어하지 못한 사람의 수
        for stage in stages:
            if stage == i:
                count += 1
        if count == 0:
            dict[i] = 0
        else:
            dict[i] = (count/player)
        
        player -= count
    
    answer = sorted(dict, key = lambda x : dict[x], reverse = True)
    return answer

