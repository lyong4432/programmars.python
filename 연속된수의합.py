def solution(num, total):
    answer = []
    a1 = (((2 * total) // num ) - num + 1)//2
    for i in range(a1, a1+num):
        answer.append(i)
    return answer

# 등차수열
