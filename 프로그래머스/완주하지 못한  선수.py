def solution(participant, completion):
    
    participant_sort = sorted(participant)
    completion_sort = sorted(completion)
    
    for p, c in zip(participant_sort, completion_sort):
        if p != c:
            return p
        
    return participant_sort[-1]