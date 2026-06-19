def solution(genres, plays):
    gp = {}
    
    for i in range(len(genres)):
        g = genres[i]
        gp.setdefault(g,[])
        gp[g].append([plays[i] , i])
        
    g_sum = {}
    for g in gp:
        g_sum[g] = sum(x[0] for x in gp[g] )
        
    for g in gp:
        gp[g].sort(key = lambda x: (-x[0],x[1]))
    
    sort_genres = sorted(g_sum , key = lambda x: -g_sum[x])
    
    answer = []
    for p in sort_genres:
        for i in gp[p][:2]:
            answer.append(i[1])
    
                
    return answer