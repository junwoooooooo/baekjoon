def solution(nums):
    max_num = len(nums) // 2
    answer = 0
    m = len(set(nums))
    
    if m >= max_num:
        answer = max_num
        
    else:
        answer = m
    
    return answer