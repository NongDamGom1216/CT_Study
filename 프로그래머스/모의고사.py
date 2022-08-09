# 1단계

# 정답 참고

def solution(answers):
    answer = []
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]

    for i in range(len(answers)):

        if answers[i] == supo_1[i % 5]:
            cnt[0] += 1

        if answers[i] == supo_2[i % 8]:
            cnt[1] += 1

        if answers[i] == supo_3[i % 10]:
            cnt[2] += 1

    max_cnt = max(cnt)

    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i + 1)

    return answer