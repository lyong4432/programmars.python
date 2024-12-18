def solution(chicken):
    result = []
    left = 0
    left1 = 0
    while chicken > 0:
        
        temp = chicken // 10
        left += (chicken - temp*10) 
        result.append(temp)
        chicken //= 10

    while left > 0:
        
        temp = left // 10
        left1 += (left - temp*10) 
        result.append(temp)
        left //= 10

    return sum(result) + left1 // 10
