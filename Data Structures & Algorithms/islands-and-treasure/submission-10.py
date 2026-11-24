class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dist = 0

        q = deque()
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS
                        or grid[row][col] == -1 or (row, col) in visit):
                        continue
                    grid[row][col] = dist
                    q.append((row, col))
                    visit.add((row, col))
            dist += 1