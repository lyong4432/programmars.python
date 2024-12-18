def solution(A, B):
    answer = 0
    if A==B: answer = 0
    else:  
        answer = check(A,B)
    return answer

def check (A,B):
    n = len(A)
    cnt =0
    for i in range(0, n):
        if A == B: return cnt
        else: 
            A = A[-1] + A[0:n-1]
            print(A)
            cnt += 1
    
    if A != B: return -1
