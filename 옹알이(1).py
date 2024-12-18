def solution(babbling):
    answer = 0
    patterns = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        b = b.replace('aya', '1').replace('ye', '1').replace('woo', '1').replace('ma','1')
        b = b.replace('1','')
        if b == '': answer += 1
    return answer
