n = int(input())
lst = [] 

for i in range(n):
    a, b = map(int,input().split())
    lst.append([a,b])
    
lst.sort(key=lambda x: (x[1], x[0]))

count = 0
endtime = 0
for s,e in lst:
    if s >= endtime:
        endtime = e
        count += 1
    

            
print(count)