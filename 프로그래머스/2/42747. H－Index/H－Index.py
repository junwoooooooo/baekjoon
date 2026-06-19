def solution(citations):
    n = len(citations)
    
    for h in range(n,-1,-1):
        count = 0
        
        for i in citations:
            if i >= h:
                count += 1
                
        if count >= h:
            return h
            
        
            
    