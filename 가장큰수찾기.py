def solution(array):
    maxNumber = max(array)
    maxIndex = array.index(maxNumber)
    return [maxNumber, maxIndex]
