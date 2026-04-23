import heapq

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

total = 0
for _ in range(n - 1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    s = a + b
    total += s
    heapq.heappush(heap, s)

print(total)