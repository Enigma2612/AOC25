with open('7.txt') as f:
    data = f.read()


grid = [list(i) for i in data.splitlines()]

num_ways = {}

S = (0, grid[0].index('S'))
beams = [S]

ans = 0

def add(r, c):
    beams.append((r,c))
    num_ways[(r,c)] = num_ways.get((r,c), 0) + 1

while beams:
    r,c = beams.pop()
    if r >= len(grid):
        continue

    if grid[r][c] in '.S':
        add(r+1, c)

    if grid[r][c] == '^':
        add(r, c+1)
        add(r, c-1)


for c in range(len(grid[-1])):
    ans += num_ways.get((len(grid)-1, c), 0)

print(ans)


#Very slow, not efficient, but works


