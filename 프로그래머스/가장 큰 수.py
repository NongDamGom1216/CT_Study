# 2단계

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # 숫자 뒤에 0이 들어가는 경우를 해결하기 위함
    # 333 303030 343434 555 999에서 앞 자리만 비교한다

    return str(int(''.join(numbers)))