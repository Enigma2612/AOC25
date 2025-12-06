with open('5.txt') as f:
    data = f.read().partition('\n\n')

lowers = [int(i.partition('-')[0]) for i in data[0].splitlines()]
uppers = [int(i.partition('-')[2]) for i in data[0].splitlines()]

ranges_dic = {}

for i in range(len(lowers)):
    ranges_dic[lowers[i]] = max(uppers[i], ranges_dic.get(lowers[i],0))

sorted_lowers = sorted(list(set(lowers)))


for i in range(1,len(sorted_lowers)):
    a = sorted_lowers[i-1]
    b = sorted_lowers[i]
    if b <= ranges_dic[a]:
        ranges_dic[a] = max(ranges_dic[a], ranges_dic[b])
        del ranges_dic[b]
        sorted_lowers[i] = a
ans = 0

for r in ranges_dic:
    ans += ranges_dic[r] - r + 1

print(ans)
