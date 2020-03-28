def wallsAndGates(self, rooms):
    EMPTY = 2147483647
    row = len(rooms)
    col = len(rooms[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    q = []
    for r in range(row):
        for c in range(col):
            if rooms[r][c] == 0:
                q.append((r,c))
    while len(q) > 0:
        point = q.pop(0)
        x = point[0]
        y = point[1]
        for d in directions:
            r = x + d[0]
            c = y + d[1]
            if r < 0 or r >= row or c<0 or c>=col or rooms[r][c] != EMPTY:
                 continue
            rooms[r][c] = rooms[r][c] + 1
            q.append((r,c))

from collections import deque
def wallsAndGatesV2(srooms):
    '''
    Do not return anything, modify room in-place instead.
    '''
    if not rooms:
        return
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    rows, cols = len(rooms), len(rooms[0])
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r,c))
    while q:
        row, col = q.popleft()
        dist = rooms[row][col] + 1
        for dy,dx in directions:
            r = row + dy
            c = col + dx
            if r >=0 and 0 <= c < cols and rooms[row][col] == 2147483647:
                rooms[row][col] = dist
                q.append((row,col))