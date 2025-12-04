with open('Side Quests/joltage.txt') as f:
    data = f.read()

adapters_list = sorted(list(map(int, data.splitlines())))
adapters_list.insert(0,0)

diff = {1:0, 2:0, 3:1}

diff_list = [1] + [-1 for _ in range(len(data.splitlines())-1)] + [3]

for i in range(len(adapters_list)-1):
    difference = adapters_list[i+1] - adapters_list[i]
    diff[difference] += 1
    diff_list[i+1] = difference

print(diff[1]*diff[3])
print(adapters_list)
print(diff)