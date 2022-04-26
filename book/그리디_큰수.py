"""
첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보나 작거나 같다.

다양한 수로 이루저진 배열이 있을 때 M번 더하여 가장 큰 수를 구하는 것이다. 단 같은 수는 연속으로 3번을 초과할 수 없다.

입력 예시 :
5 8 3
2 4 5 4 6

출력 예시 :
46

"""
from unittest import result


n, m, k = map(int, input().split()) # 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째 큰 수

# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)