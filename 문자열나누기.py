def solution(s):

    answer = 0
    while s:
        print(s,end=' ')
        if(len(s)==1): 
            answer += 1
            break
        else:
            xo = 1
            xx = 0
            x = s[0]
            check = 0
            for i in range(1,len(s)):
                if (x == s[i]) : xo += 1
                else: xx += 1
                if xo == xx: 
                    s = s[i+1:]
                    answer += 1
                    check = 1
                    break
            if (check == 0): 
                answer += 1
                break
            

    return answer
