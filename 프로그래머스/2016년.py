# 1단계

def solution(a, b):
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 1월 1일이 금요일, index 1이 금요일이 나오게
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = date[(sum(month[:a-1])+b)%7]
    # 전달까지의 요일 수 + 구하고자 하는 요일 수
    return answer

print(solution(5,24))