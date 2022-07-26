# 프로그래머스 1단계

def solution(lottos, win_nums):
    answer = []
    
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} #맞은 갯수:등수
    
    count_min = 0 #번호가 일치하는 최솟값
    count_zero = 0 #0의 갯수
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count_min += 1
        if lottos[i] == 0:
            count_zero += 1
    
    count_max = count_min + count_zero #번호가 일치하는 최댓값
    
    answer = [rank[count_max], rank[count_min]]
    
    
    return answer