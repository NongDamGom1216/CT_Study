# 2단계

def solution(priorities, location):
    
    index_array = [i for i in range(len(priorities))]
    copy_array = priorities.copy()
    
    i = 0
    
    while True:
        if copy_array[i] < max(copy_array[i+1:]):
            index_array.append(index_array.pop(i)) # 인수보다 큰 값이 있으면 pop으로 맨 뒤로 보냄
            copy_array.append(copy_array.pop(i)) # max 값보다 작으면 맨 뒤로 보냄
            
        else:
            i += 1
            
        if copy_array == sorted(copy_array, reverse = True):
            break
            # 높은 순으로 정렬한 것과 같아지면 break
    
    return index_array.index(location) + 1
    # index 요소로 찾는 법