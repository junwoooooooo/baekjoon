from collections import deque

def solution(m, n, h, w, drops):
    INF = float('inf')

    # drop_time[R][C] = 그 점에 처음 떨어진 시각 (없으면 INF)
    drop_time = [[INF] * n for _ in range(m)]
    for t, (R, C) in enumerate(drops, start=1):
        if drop_time[R][C] == INF:
            drop_time[R][C] = t

    # 1) 가로 방향 슬라이딩 최소 (윈도우 너비 w)
    tmp = [[0] * (n - w + 1) for _ in range(m)]
    for r in range(m):
        dq = deque()
        row = drop_time[r]
        for c in range(n):
            while dq and row[dq[-1]] >= row[c]:
                dq.pop()
            dq.append(c)
            if dq[0] <= c - w:
                dq.popleft()
            if c >= w - 1:
                tmp[r][c - w + 1] = row[dq[0]]

    # 2) 세로 방향 슬라이딩 최소 (윈도우 높이 h)
    W = n - w + 1
    wet = [[0] * W for _ in range(m - h + 1)]
    for c in range(W):
        dq = deque()
        for r in range(m):
            while dq and tmp[dq[-1]][c] >= tmp[r][c]:
                dq.pop()
            dq.append(r)
            if dq[0] <= r - h:
                dq.popleft()
            if r >= h - 1:
                wet[r - h + 1][c] = tmp[dq[0]][c]

    # 3) 가장 늦게 젖는 칸 = 답 (INF는 안 젖는 칸이라 그대로 최댓값)
    best_time = -1
    best = [0, 0]
    for r in range(m - h + 1):
        for c in range(W):
            if wet[r][c] > best_time:
                best_time = wet[r][c]
                best = [r, c]
    return best