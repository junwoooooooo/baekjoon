def solution(genres, plays):
    gp = {}
    
    for i in range(len(genres)):
        g = genres[i]
        gp.setdefault(g,[])
        gp[g].append([plays[i],i])
        
    total = {}
    for g in gp:
        total[g] = sum(x[0] for x in gp[g])
        
    for g in gp:
        gp[g].sort(key = lambda x: (-x[0],x[1]))
        
        
    sorted_genres = sorted(total, key=lambda g: -total[g])
                
    answer = []        
    for g in sorted_genres:
        for x in gp[g][:2]:
            answer.append(x[1])
            
        
        
        
        
    return answer