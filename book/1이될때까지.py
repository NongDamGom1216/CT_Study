"""
그리디

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값 출력
입력 예시

25 5

출력 예시
2

입력 예시
25 3

출력 예시
6

"""

n,k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # n이 k보다 작을 때(더 이상 나눌 수 없을 때 탈출)
    if n < k:
        break

    # k로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)