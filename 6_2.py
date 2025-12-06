with open('6.txt') as f:
    data = f.read()

lines = data.splitlines()

ans = 0

num_probs = len(lines[0].strip().split())
num_places = len(lines[0])
num_vals = len(lines)

problems = []
operations = lines[-1].split()

problem = []
for i in range(num_places):
    flag = False
    s = ''
    for j in range(num_vals-1):
        if lines[j][i].isdigit():
            flag = True
        s += lines[j][i]
    if flag:
        problem.append(s)
    else:
        problems.append(problem)
        problem = []

else:
    problems.append(problem)


for i in range(num_probs):
    prob = problems[i]

    op = operations[i]

    if op == '*':
        sol = 1
        for val in prob:
            sol *= int(val)
    else:
        sol = 0
        for val in prob:
            sol += int(val)

    ans += sol

print(ans)

    