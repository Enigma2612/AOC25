with open('4.txt') as f:
    data = f.read()

grid_raw = data.splitlines()

grid = [list(i) for i in grid_raw]

n_rows = len(grid)
n_cols = len(grid[0])

ans = 0


def check_neighbours(i,j):
    n = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if x==y==0: continue
            if 0 <= (x+i) < n_cols and 0 <= (y+j) < n_rows:
                if grid[y+j][x+i] in '@x':
                    n +=1
    return n

ans_this_round = 1

while ans_this_round:
    ans_this_round = 0

    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(row):
            if col in '@' and check_neighbours(col_num, row_num) < 4:
                ans_this_round += 1
                grid[row_num][col_num] = 'x'

    for row_num, row in enumerate(grid):
            for col_num, col in enumerate(row):
                if col == 'x':
                    grid[row_num][col_num] = '.'
    
    ans += ans_this_round



print(ans)


