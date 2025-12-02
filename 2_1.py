with open('2.txt') as f:
    data = f.read()

ranges = data.split(',')
ans = 0

for i in ranges:
    start,end = i.split('-')
    for j in range(int(start), int(end)+1):
        s = str(j)
        n = len(s)
        if n%2: continue
        s1 = s[:(n)//2]
        s2 = s[(n)//2:]
        if s1 == s2:
            ans += j

print(ans)