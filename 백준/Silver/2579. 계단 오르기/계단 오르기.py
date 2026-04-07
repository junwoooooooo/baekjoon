n = int(input())
score = [0]
data = [[0,0,0] for _ in range(n+1)]

for i in range(n):
    s = int(input())
    score.append(s)
    
for i in range(0,n):
    if i == 0:
        data[1][1] = score[1]
        data[1][2] = 0
        continue
    if i == 1:
        data[2][1] = score[2]
        data[2][2] = score[1]+score[2]
        continue
        
    data[i+1][2] = score[i+1] + data[i][1]
    data[i+1][1] = max((score[i+1] + data[i-1][1]),(score[i+1] + data[i-1][2]))
    
print(max((data[n][2]),(data[n][1])))
    
    
    
    