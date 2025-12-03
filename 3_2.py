with open("3.txt") as f:
    data = f.read()

banks = data.splitlines()
ans = 0

total_len = len(banks[0])

nos = 12

for bank in banks:
    num_str = ''
    prev_pointer = 0
    for no in range(nos):
        max_num = '0'
        for i in range(prev_pointer, (total_len - nos + no + 1)):
            if bank[i] > max_num:
                max_num = bank[i]
                prev_pointer = i+1
        num_str += max_num
    ans += int(num_str)

print(ans)
