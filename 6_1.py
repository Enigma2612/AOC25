with open('6.txt') as f:
    data = f.read()

lines = data.splitlines()

ans = 0

num_probs = len(lines[0].strip().split())
num_vals = len(lines)

problems = [['' for i in range(num_vals-1)] for j in range(num_probs)]
operations = lines[-1].split()

for i in range(num_vals-1):
    line = lines[i].split()
    for j in range(num_probs):
        problems[j][i] = line[j]

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

    