# 1단계

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        first = commands[i][0] - 1
        last = commands[i][1]
        index = commands[i][2] - 1
        
        answer.append(sorted(array[first:last])[index])
    
    return answer