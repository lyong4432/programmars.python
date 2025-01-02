def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    supoScore = [0,0,0]
    for idx in range(len(answers)):
        if answers[idx] == supo1[idx%5]: supoScore[0] += 1
        if answers[idx] == supo2[idx%8]: supoScore[1] += 1
        if answers[idx] == supo3[idx%10]: supoScore[2] += 1
    maxScore = max(supoScore)
    for i in range(len(supoScore)):
        if maxScore == supoScore[i]: answer.append(i+1)
    return answer
