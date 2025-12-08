with open('7.txt') as f:
    data = f.read()


grid = [list(i) for i in data.splitlines()]


S = (0, grid[0].index('S'))
beams = [S]
checked = {S}

ans = 0

def add(r, c):
    if (r, c) in checked: return
    checked.add((r,c))
    beams.append((r,c))


while beams:
    r,c = beams.pop()
    if r >= len(grid):
        continue

    if grid[r][c] in '.S':
        add(r+1, c)

    if grid[r][c] == '^':
        add(r, c+1)
        add(r, c-1)
        ans += 1

print(ans)
    


