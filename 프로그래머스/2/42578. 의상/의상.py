def solution(clothes):
    closet = {}
    
    for i , j in clothes:
        if j in closet:
            closet[j] += 1
        else:
            closet[j] = 1
            
    answer = 1
    for i in closet.values():
        answer *= (i+1)
        
        
    
    return answer-1