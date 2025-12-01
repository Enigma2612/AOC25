with open('1.txt') as f:
    data = f.read()

cmds = data.splitlines()

start = 50

ans = 0
d = {'L':-1, 'R':1}

for cmd in cmds:
    if cmd[0] == 'R':
        ans += (int(cmd[1:]) + start)//100
    else:
        x = int(cmd[1:])
        if start == 0:
            ans += x // 100   
        else: 
            q, r = divmod(x, 100)
            ans += q + (1 if r >= start else 0)


    start += d[cmd[0]]*int(cmd[1:])
    start %= 100


print(ans)