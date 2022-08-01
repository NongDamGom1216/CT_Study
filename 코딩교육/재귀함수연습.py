from numpy import rec

# 재귀 함수 반복 예제
def recursive_function(i):
    # 100번 째에 종료
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '재귀 함수 호출')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

# recursive_function(1)


# 팩토리얼 예제(재귀함수)
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

def normal_factorial(num):
    total = 1
    for i in range(1, num + 1): # 범위 헷갈릴 수 있음
        total *= i
    return total

# print(factorial(5))

print(normal_factorial(5))