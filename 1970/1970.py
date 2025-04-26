from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        # Precalc: día en que cada celda se inunda (1…row*col)
        time_grid = [[0]*col for _ in range(row)]
        for day, (r, c) in enumerate(cells, start=1):
            time_grid[r-1][c-1] = day

        # DIRECCIONES
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # Binsearch sobre el día máximo que aún permite cruzar
        low, high = 1, row*col
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            # BFS para verificar si se puede cruzar
            visited = [[False]*col for _ in range(row)]
            q = deque()
            for j in range(col):
                if time_grid[0][j] > mid:
                    visited[0][j] = True
                    q.append((0, j))

            can = False
            while q:
                x, y = q.popleft()
                if x == row-1:
                    can = True
                    break
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < row and 0 <= ny < col:
                        if not visited[nx][ny] and time_grid[nx][ny] > mid:
                            visited[nx][ny] = True
                            q.append((nx, ny))

            # Ajustar binsearch según resultado
            if can:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


