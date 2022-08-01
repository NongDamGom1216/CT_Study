# 문자열 배열을 받아 에너그램 단위로 그룹핑하라.

# 입력 : ["eat", "tea", "tan", "ate", "nat", "bat"]

example = ["eat", "tea", "tan", "ate", "nat", "bat"]

import collections

def anagram(words):

    result = collections.defaultdict(list)

    for i in words:
        sorted_word = "".join(sorted(i)) # 정렬하여 사전에 추가
        result[sorted_word].append(i)
    
    return print(result.values())

anagram(example)


# result = collections.defaultdict(list)

# for i in example:
#     sorted_word = "".join(sorted(i))
#     result[sorted_word].append(i)

# print(result)

# 위를 실행하면
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})