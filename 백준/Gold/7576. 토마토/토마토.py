from collections import deque

m,n = map(int,input().split())
tmtmap = []
find = deque()

for i in range(n):
    tmtlis =list(map(int,input().split()))
    tmtmap.append(tmtlis)
    
for i in range(n):
    for j in range(m):
        if tmtmap[i][j] == 1:
            find.append([i,j])
        
dxy = [[0,1],[1,0],[0,-1],[-1,0]]

def tmt():    
    while find:
        i, j = find.popleft()
        for k in range(4):
            ni = dxy[k][0] + i
            nj = dxy[k][1] + j
            
            if 0 <= ni < n and 0 <= nj < m and tmtmap[ni][nj] == 0 :
                tmtmap[ni][nj] = tmtmap[i][j] + 1
                find.append([ni , nj])
                
tmt()
maxnum = 0
for i in range(n):
    if 0 in tmtmap[i]:
        print(-1)
        break
    for j in range(m):         
        maxnum = max(maxnum, tmtmap[i][j])
else:
    print(maxnum - 1)
        
        
        
       