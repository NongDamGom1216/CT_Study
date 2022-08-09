# 2단계

def solution(people, limit):
    count = 0
    
    people.sort()

    start = 0
    end = len(people) - 1
    
    # 몸무게를 가장 큰 사람과 작은 사람을 비교해가며
    # limit이 넘으면 한 사람만 태운다.
    # 50 50 70 80 -> 배 1개, 50 + 80 <= 100 (x), 80만 태움
    # 배 2개, 50 + 70 <= 100 (x), 70만 태움
    # 배 3개, 50 + 50 <= 100 (o), 같이 태움
    
    while start <= end:
        count += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
            
    return count