# 1단계

def solution(n, arr1, arr2):
    answer = []
    bin_array = []
    
    array = list(zip(arr1, arr2))
    
    for i, j in array:
        bit = i | j
        bin_array.append(bin(bit)[2:].zfill(n))
    
    for i in bin_array:
        string = i.replace("1","#").replace("0"," ")
        answer.append(string)
    
    return answer