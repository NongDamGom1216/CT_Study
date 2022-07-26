# 프로그래머스 오픈채팅방 lv2

def solution(record):
    answer = []
    user = {}
    states = [] #Enter, Leave, Change
    
    for i in record:
        split_record = i.split(" ")
        state = split_record[0]
        userid = split_record[1]
        
        if state in ("Enter", "Change"):
            name = split_record[2]
            user[userid] = name
        states.append((state, userid))
        
    for i in states:
        state = i[0]
        userid = i[1]
    
        if state == "Enter":
            answer.append(f"{user[userid]}님이 들어왔습니다.")

        elif state == "Leave":
            answer.append(f"{user[userid]}님이 나갔습니다.")
    
    
    return answer