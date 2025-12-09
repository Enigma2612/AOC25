with open('7.txt') as f:
    data = f.read()


grid = [list(i) for i in data.splitlines()]

num_ways = [[0 for c in range(len(grid[0]))] for r in range(len(grid))]

S = (0, grid[0].index('S'))
beams = [S]

def num_ways_after(r,c):

    if r >= len(grid)-1:
        num_ways[r][c] = 1
        return 1

    if num_ways[r][c]: return num_ways[r][c]

    if grid[r][c] in '.S':
        num_ways[r][c] = num_ways_after(r+1, c)
        return num_ways[r][c]

    if grid[r][c] in '^':
        num_ways[r][c] = num_ways_after(r, c+1) + num_ways_after(r, c-1)
        return num_ways[r][c]
    

print(num_ways_after(*S))

    