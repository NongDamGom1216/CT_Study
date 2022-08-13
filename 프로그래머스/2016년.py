# 1단계

def solution(a, b):
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 1월 1일이 금요일, index 1이 금요일이 나오게
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = date[(sum(month[:a-1])+b)%7]
    # 전달까지의 요일 수 + 구하고자 하는 요일 수
    return answer

# 2022년
def solution2(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 2022년 1월 1일이 토요일, index 1이 금요일이 나오게
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = date[(sum(month[:a-1])+b)%7]
    # 전달까지의 요일 수 + 구하고자 하는 요일 수
    return answer

result = solution2(8,11)

print(result)


# 1000일 후의 날짜 계산
import datetime

def solution_date(year, month, day , n):
    day = datetime.date(year, month, day)
    theday = day + datetime.timedelta(n)
    return theday

print(solution_date(2021,5,10,1000))

# 요일 구하는 다른 방법
weekdays = ['일','월','화','수','목','금','토']
def dayOfWeek(y, m, d):
    t1 = y - (14-m) // 12
    t2 = t1 + (t1//4) - (t1//100) + (t1//400)
    t3 = m + 12 * ((14-m) //12) -2
    return (d+t2+(31*t3//12)) % 7

year, month, day = 2022,8,11
res = dayOfWeek(year,month,day)

print(f'{weekdays[res]}요일')