import copy

def solution(triangle):
    answer = copy.deepcopy(triangle) 
    for i in range(len(triangle)-1):
        for j in range(i +1):

            triangle[i+1][j]   = max(triangle[i+1][j],   triangle[i][j] + answer[i+1][j])
            triangle[i+1][j+1] = max(triangle[i+1][j+1], triangle[i][j] + answer[i+1][j+1])

    

    return max(triangle[-1])

