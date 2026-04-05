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

"""
1.num은 노드 수를 뜻하고 line은 연결수를 뜻한다
2.linemap이라는 2차원 리스트를 호출한다
3.양방향 노드이므로 a에해당하는 노드에 b를 연결한다
ex) 1 2 의 연결을 받아서 linemap[1].append(2) , linemap[2].append(1) 이런식으로 저정하면 나중에 1이나 2에관련된 연결을 호출하기 편하다
4.visited에 대한 리스트는 실제로 간 노드인지 아닌지를 구별하기 위해 쓰인다 popleft로 현재 노드를 호출한다음 visited = True 처리를 해야한다
5.  deque[1]을 통해서 1과 연결되어 있는 노드를 호출한다
6. 가장 왼쪽에 있는 노드부터 now에 넣고 visited를 통해 했던 노드인지 아닌지를 판별하고 만약 방문한곳이 아니라면 wait에 넣고 나중에 popleft를 통해 인접노드를 호출할 것이다
7.문제에서는 1을 통해 감염된 컴퓨터 수를 구하는것이므로 실제로 print를 할때는 1을 빼서 출력해야한다
"""
                
                
            
            
        
    
    

