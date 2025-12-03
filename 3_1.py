with open("3.txt") as f:
    data = f.read()

banks = data.splitlines()

ans = 0

for bank in banks:
    p1 = 0
    p2 = 1
    num = 0
    while p2 < len(bank):
        num2 = 10*int(bank[p1]) + int(bank[p2])
        num = max(num2, num)

        if int(bank[p2]) > int(bank[p1]):
            p1 = p2
        p2 += 1
        
    ans += num

print(ans)
