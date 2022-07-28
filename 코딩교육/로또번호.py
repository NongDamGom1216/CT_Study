# 로또 번호 자동 생성기
import random

count = int(input())

print(f'게임 수 : {count}')


# 내가 혼자 짜본 코드

# for i in range(count):
#     array = []
#     for j in range(6):
#         now_x = random.randrange(1,46)
        
#         # 중복 체크 필요
#         array.append(now_x)

#     print(array)


# 피드백 결과
for i in range(0, int(count)):
    lotto = random.sample(range(1,46), 6)
    lotto.sort()
    print(lotto)
