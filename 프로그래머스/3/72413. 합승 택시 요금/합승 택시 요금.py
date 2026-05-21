import heapq

def solution(n, s, a, b, fares):
    graph = [[] for i in range(n+1)]
    for c, d, fare in fares:
        graph[c].append((d, fare))
        graph[d].append((c, fare))
        
    def mindis(start):
        inf = 10**10
        dist = [inf for _ in range(n+1)]
        dist[start] = 0
        
        heap = []
        heapq.heappush(heap, (0, start))
        
        while heap:
            cost, now = heapq.heappop(heap)
            
            if cost > dist[now]:
                continue
                
            for next_node, fare in graph[now]:
                next_cost = cost + fare
                
                if next_cost < dist[next_node]:
                    dist[next_node] = next_cost
                    heapq.heappush(heap, (next_cost, next_node))
                    
        return dist
                    
    dist_s = mindis(s)   
    dist_a = mindis(a)  
    dist_b = mindis(b)   
    
    answer = 10**10
    for k in range(1, n + 1):
        answer = min(
            answer,
            dist_s[k] + dist_a[k] + dist_b[k]
        )
    return answer