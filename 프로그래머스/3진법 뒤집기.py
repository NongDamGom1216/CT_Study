# 1단계

def solution(n):
    answer = ''
    while n > 0:
        n,r = divmod(n,3) # 몫과 나머지를 튜플형으로 반환
        answer += str(r)
    return int(answer, 3)
    # 3진법으로 구성된 answer를 10진법으로 바꿔줌