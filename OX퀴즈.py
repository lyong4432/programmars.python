def solution(quiz):
    answer = []
    for q in quiz:
        nums = q.split(' ')
        ans1 = int(nums[4])
        if nums[1] == '+':
            ans2 = int(nums[0]) + int(nums[2])
        else: ans2 = int(nums[0]) - int(nums[2])
        
        if (ans1 == ans2) : answer.append('O')
        else: answer.append('X') 
    
    return answer
