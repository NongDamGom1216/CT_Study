T = int(input())
result = 0

for i in range(1, T+1):
    for k in list(map(int, input().split())):
        if k % 2:
            result += k
    
    print(f'#{i} {result}')