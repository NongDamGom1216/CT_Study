# 1단계

def solution(numbers):
    answer = []
    
    for i in numbers:
        for j in numbers[numbers.index(i)+1:]:
            sum = i + j
            if sum not in answer:
                answer.append(sum)
    
    answer.sort()
    
    return answer