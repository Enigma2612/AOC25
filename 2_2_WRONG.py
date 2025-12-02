with open('2.txt') as f:
    data = f.read()

ranges = data.split(',')
ans = 0

def is_repeating(s):
    stack = []
    ind = 0
    rep = 0
    rep_times = 1
    for i in s:
        print(stack)
        print(ind)
        print(rep)
        print(rep_times)
        if not stack:
            stack.append(i)
            rep += 1
            continue
        if stack[ind] == i:
            ind = (ind+1)%rep
            if ind == 0:
                rep_times += 1
            stack.append(i)
        else:
            stack.append(i)
            ind = 0
            rep = len(stack)
            rep_times = 1
    
    return rep_times > 1 and not ind

print(is_repeating(str(101101)))

for i in ranges:
    start,end = i.split('-')
    for j in range(int(start), int(end)+1):
        s = str(j)
        if is_repeating(s):
            ans += j

print(ans)


#FAILS FOR NUMBERS OF FORM XYXXYX (Fails for at least these numbers)

