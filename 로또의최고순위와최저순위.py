def solution(lottos, win_nums):
    countZero, countSame = 0,0
    rank = {
        0:6, 1:6 , 2:5, 3:4, 4:3, 5:2, 6:1
    }
    
    countZero = 0
    for i in range(6):
        if lottos[i] == 0: countZero += 1
        elif lottos[i] in win_nums: countSame += 1
    
    
    
    
    return [ rank[countZero+countSame], rank[countSame]]
