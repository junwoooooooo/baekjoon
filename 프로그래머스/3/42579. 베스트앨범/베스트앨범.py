def solution(genres, plays):
    gp = {}
    
    for i in range(len(genres)):
        p = genres[i]
        gp.setdefault(p , [])
        gp[p].append([plays[i], i])
        
    s_genres = {}
    for g in gp:
        s_genres[g] = sum(x[0]for x in gp[g])
        
    for g in gp:
        gp[g].sort(key=lambda x: (-x[0], x[1]))
        
    s_genres_sort = sorted(s_genres, key=lambda x: -s_genres[x])
    
    answer = []
    for p in s_genres_sort:
        for x in gp[p][:2]:
            answer.append(x[1])
                
    return answer