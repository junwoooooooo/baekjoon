n = int(input())
rgbmap = []
minrgb = [[0,0,0]for _ in range(n)] 
for i in range(n):
    r, g , b = map(int,input().split())
    rgbmap.append([r,g,b])
    
for i in range(n):
    if i == 0 :
        minrgb[0][0] = rgbmap[0][0]
        minrgb[0][1] = rgbmap[0][1]
        minrgb[0][2] = rgbmap[0][2]
        continue
        
    minrgb[i][0] = min(minrgb[i-1][1],minrgb[i-1][2]) + rgbmap[i][0]
    minrgb[i][1] = min(minrgb[i-1][2],minrgb[i-1][0]) + rgbmap[i][1]
    minrgb[i][2] = min(minrgb[i-1][0],minrgb[i-1][1]) + rgbmap[i][2]
    
answer = min(minrgb[n-1][0],minrgb[n-1][1],minrgb[n-1][2])
print(answer)