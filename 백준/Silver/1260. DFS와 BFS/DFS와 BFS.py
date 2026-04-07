from collections import deque 
node , line , start = map(int , input().split())
nummap = [ [] for _ in range(node+1)]
visited = [False]*(node+1)
for i in range (line):
    a,b = map(int, input().split())
    nummap[a].append(b)
    nummap[b].append(a)

for i in range(node+1):
    nummap[i].sort()

def dfs(n):
    visited[n] = True
    print(n , end = ' ')

    for i in nummap[n]:
        if visited[i] == False:
            dfs(i)
def bfs(n):
    visited[n] = True
    numque = deque([n])

    while numque:
        now = numque.popleft()
        print(now , end = ' ')

        for i in nummap[now]:
            if not visited[i]:
                visited[i] = True
                numque.append(i)   

dfs(start)
print()
visited = [False] * (node+1) 
bfs(start)