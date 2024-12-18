def solution(my_string):
    answer = 0
    mark = ''
    nums = my_string.split(' ')
    for idx, n in enumerate(nums):
        if idx == 0: answer = int(n)
        else:
            if n.isdigit():
                if mark =='+': 
                    answer += int(n)
                elif mark == '-': 
                    answer -= int(n)
            else: 
                mark = n
            
    return answer
