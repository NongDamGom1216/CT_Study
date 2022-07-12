from cgi import test

T = int(input())

DAY = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

for test_case in range(1, T + 1):
    day = input()
    if day=="SUN":
        print(f'#{test_case} 7')
        continue
    next_day=6-DAY.index(day)
    print(f'#{test_case} {next_day}')
    
