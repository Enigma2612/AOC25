with open('2.txt') as f:
    data = f.read()

ranges = data.split(',')
ans = 0

def is_repeating(s):
    s = str(s)
    n = len(s)
    for L in range(1,n//2+1):
        if not n%L and s[:L]*(n//L) == s:
            return True
    return False

for i in ranges:
    start,end = i.split('-')
    for j in range(int(start), int(end)+1):
        s = str(j)
        if is_repeating(s):
            ans += j

print(ans)
