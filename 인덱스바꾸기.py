def solution(my_string, num1, num2):
    answer = ''
    n1 = my_string[num1]
    n2 = my_string[num2]
    for idx, n in enumerate(my_string):
        if idx == num1:
            answer += n2
        elif idx == num2:
            answer += n1
        else: answer += n
        
    return answer
