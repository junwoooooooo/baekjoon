n , maxbag = map(int , input().split())
baglist = []
maxvalue = [[0]*(maxbag+1) for _ in range(n)]

for i in range(n):
    w , v = map(int,input().split())
    baglist.append([w,v])
    

for i in range(n):
    for j in range(maxbag+1):
        if i == 0 and j >= baglist[i][0]:
            maxvalue[i][j] = baglist[i][1]
            continue
        if j >= baglist[i][0]:    
            maxvalue[i][j] = max(maxvalue[i-1][j],maxvalue[i-1][j-baglist[i][0]]+baglist[i][1])
        else:
            maxvalue[i][j] = maxvalue[i-1][j]
            
print(maxvalue[n-1][maxbag])