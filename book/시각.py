"""
113p 4-2

완전탐색유형
"""

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 00시 00분 00초부터 h시 59분 59초 까지의 시각 중에서 3이 포함된 횟수
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

