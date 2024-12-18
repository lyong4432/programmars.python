def solution(babbling):
    answer = 0
    patterns = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for idx, p in enumerate(patterns):
            bab = bab.replace(p, str(idx))
        if bab.isdigit():
            pre = bab[0]
            flag = 1
            for i in range(1,len(bab)):
                if pre == bab[i]:
                    flag = 0
                    break 
                else: 
                    pre = bab[i] 
            if flag : answer += 1
    return answer
