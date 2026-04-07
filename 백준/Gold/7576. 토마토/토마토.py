from collections import deque
m, n = map(int, input().split())      
tmtmap = []                          
find = deque()

for i in range(n):                   
    tmtlist = list(map(int, input().split()))
    tmtmap.append(tmtlist)
    
for i in range(n):                    
    for j in range(m):
        if tmtmap[i][j] == 1:
            find.append([i, j])      
            
dxy = [[0,1],[1,0],[0,-1],[-1,0]]

def tmt():
    while find:                       
        i, j = find.popleft()        
        for k in range(4):            
            dx = dxy[k][0]
            dy = dxy[k][1]
            if 0 <= dx+i < n and 0 <= dy+j < m and tmtmap[dx+i][dy+j] == 0: 
                tmtmap[dx+i][dy+j] = tmtmap[i][j] + 1    
                find.append([dx+i, dy+j])
tmt()

for row in tmtmap:
    if 0 in row:
        print(-1)
        break
else:
    print(max(max(row) for row in tmtmap) - 1)






    
    