from collections import deque

num = int(input())
line = int(input())

linemap = [ [] for _ in range(num+1)]
for i in range(line):
    a , b = map(int,input().split())
    linemap[a].append(b)
    linemap[b].append(a)

visited = [False] * (num+1)
    
def virus():
    visited[1] = True
    wait = deque([1])
    
    while wait :
        now = wait.popleft()
        
        for i in linemap[now]:
            if visited[i] == False :
                visited[i] = True
                wait.append(i)
virus()
print(visited.count(True) - 1)
                
                
            
            
        
    
    

