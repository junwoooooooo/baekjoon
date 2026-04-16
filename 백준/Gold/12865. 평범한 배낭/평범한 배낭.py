n , k = map(int,input().split())
valuemap = []
sumap = [ [0]*(k+1) for _ in range(n)]

for _ in range(n):
    w , v =map(int,input().split())
    valuemap.append([w,v])
    
for i in range(n):
    for j in range(k+1):
        weight = valuemap[i][0]
        value = valuemap[i][1]
        if j>=weight and i==0:
            sumap[0][j] = value
            continue
        if j>=weight:
            sumap[i][j] = max(sumap[i-1][j],sumap[i-1][j-weight]+value)
        else: 
            sumap[i][j] = sumap[i-1][j]
            
print(sumap[n-1][k])