with open('5.txt') as f:
    data = f.read().partition('\n\n')

ranges = [(int(i.partition('-')[0]), int(i.partition('-')[2])) for i in data[0].splitlines()]


ans = 0
for val in data[2].splitlines():
    val = int(val)
    for r in ranges:
        if r[0] <= val <= r[1]:
            ans += 1
            break

print(ans)
