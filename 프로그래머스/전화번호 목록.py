# 2단계

def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for s1, s2 in zip(phone_book, phone_book[1:]):
        # 첫 번째 인자랑 비교하기 위함이니까 [1:] 2번째 인자부터 비교해야함
        if s2.startswith(s1): #s2가 s1으로 시작되면
            return False
    return True