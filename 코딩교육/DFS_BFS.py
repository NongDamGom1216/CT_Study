# 백준 1260

from collections import deque

n, m, v = map(int, input().split())

list = [[] for _ in range(n+1)]
# 예시 [ [],  [] ]

for _ in range(m):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)

answer_list = []

def dfs(v):
    if check[v] == 0:
        print(v, end=' ')
        check[v] = 1
        for n in sorted(list[v]):
            dfs(n)

def bfs(v):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        check[node] = 1
        for n in sorted(list[node]):
            if check[n] == 0:
                queue.append(n)
                check[n] = 1

check = [0]*(n+1)
dfs(v)

print()

check = [0]*(n+1)
bfs(v)


# https://jinho-study.tistory.com/868 참고