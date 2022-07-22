# 백준 2750

n = int(input())


array = []

for i in range(n):
    i = int(input())
    array.append(i)

sort_array = sorted(array)
for i in range(len(sort_array)):
    print(sort_array[i])

    