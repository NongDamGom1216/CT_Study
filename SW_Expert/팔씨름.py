T = int(input())



for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    result = input()
    win = 0
    for i in result:
        if i == 'o':
            win += 1

    game = 15 - len(result)
    if win + game >= 8:
        print('YES')
    else:
        print('NO')