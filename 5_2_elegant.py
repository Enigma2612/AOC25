with open('5.txt') as f:
    data = f.read().partition('\n\n')

lowers = [int(i.partition('-')[0]) for i in data[0].splitlines()]
uppers = [int(i.partition('-')[2]) for i in data[0].splitlines()]

ranges = list(zip(lowers, uppers))

ranges.sort()

merged = []
ans = 0

for (low, high) in ranges:
    if not merged:
        merged.append([low, high])
        continue
    
    last_low, last_high = merged[-1]

    if low <= last_high:
        merged[-1][1] = max(last_high, high)
    else:
        merged.append([low, high])

for low, high in merged:
    ans += high - low + 1


print(ans)
