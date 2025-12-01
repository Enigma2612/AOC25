with open('1.txt') as f:
    data = f.read()

cmds = data.splitlines()

start = 50

ans = 0
d = {'L':-1, 'R':1}

for cmd in cmds:
    start += d[cmd[0]]*int(cmd[1:])
    start %= 100
    if not start:
        ans += 1

print(ans)