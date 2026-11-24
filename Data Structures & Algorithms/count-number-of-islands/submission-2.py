class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        # depth-first search:
        # find a '1' to begin the search at
        # check all 4 directions around this '1':
        # up, down, left, right
        # exit if the cell is:
        # out of bounds
        # equal to '0'
        # already visited

        numRows = len(grid)
        numCols = len(grid[0])

        visited = set()

        def dfs(r, c):
            if ((r < 0 or r >= numRows) or
                (c < 0 or c >= numCols) or
                (grid[r][c] == '0') or
                ((r, c) in visited)):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    res += 1

        return res