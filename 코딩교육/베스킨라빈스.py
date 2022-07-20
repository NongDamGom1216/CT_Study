# 베스킨라빈스 게임
# 한번에 1~3개까지 수를 연달아 부를 수 있으며, 마지막 31을 부른 사람이 진다.

"""
컴퓨터가 무조건 시작하고, 1p는 무조건 2번째로 말한다. 컴퓨터가 무조건 이기게 만들어라

힌트 : 4n+2 공식, 31을 부르면 지는 게임이니 30을 부르면 이긴다.

컴퓨터가 무조건 4n+2 의 값을 외치게 만들기(n은 0부터)
"""

import random



# 4n + 2
def victory(call_status):
    if call_status % 4 == 0:
        computer_call = 2
    elif call_status % 4 == 1:
        computer_call = 1
    elif call_status% 4 == 3:
        computer_call = 3
    else:
        computer_call = random.randint(1, 3)

    return computer_call

call_number = 0
count = 1

while call_number < 31:

    # 무조건 컴퓨터가 시작하기 때문에 count가 2일 때 유저가 시작한다.
    if count % 2 == 0:
        print('User')

        # 갯수를 입력받아서 하는 방법
        # call_count = validate_input("호출할 개수를 입력하세요 : ", ['1', '2', '3'])

        call_count = random.randint(1, 3)
        for _ in range(call_count):
            call_number += 1
            print(f"{call_number}")

        if call_number == 31:
            break

    
    # 무조건 컴퓨터가 시작한다.
    else:
        print('Computer')
        call_count = victory(call_number)
        for _ in range(call_count):
            call_number += 1
            print(f"{call_number}")

        if call_number == 31:
            break

    count += 1

print("컴퓨터가 승리하였습니다")
# 리스트 컴프리헨션을 사용하여 32, 33은 호출에서 제외(강의 자료에 있음)




# def validate_input(prompt, valid_list):
#     while True:
#         value = input(prompt)
#         if value in valid_list:
#             value = int(value)
#             break
#         else:
#             print("잘못된 입력입니다. 재입력해주세요.")
#     return value

# 참고 https://book.coalastudy.com/python-basic/week-5/challenge-2/undefined
 






