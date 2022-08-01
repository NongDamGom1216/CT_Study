# # 문자를 입력해서 팰린드롬인지 판단하는 프로그램

example = "A man, a plan, a canal: Panama"

def palindrome(text):

    text = text.lower() # 소문자
    text = text.replace(",", "") # 특수문자 제거
    text = text.replace(":", "") # 특수문자 제거
    text = text.replace(" ", "") # 띄어쓰기 제거
    
    text_reverse = text[::-1] # 리버스

    if text == text_reverse:
        return True
    else:
        return False

print(palindrome(example))

import collections
# 참고 : https://velog.io/@lhr_06/%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EC%88%98-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%AC%B8%EC%9E%90%EC%97%B4

def palindrome_pop(text):

    deque = collections.deque()

    for i in text:
        if i.isalnum(): # 알파벳(al), 영어(num)
            deque.append(i.lower())
    
    while len(deque) > 1:
        if deque.popleft() != deque.pop(): 
            return False
    # deque.pop() : pop함
    # deque.popleft() : 반대쪽에서 pop함
    
    return True

print(palindrome_pop(example))