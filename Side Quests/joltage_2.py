with open('Side Quests/joltage.txt') as f:
    data = f.read()

adapters_list = sorted(list(map(int, data.splitlines())))
adapters_list.insert(0,0)
adapters_list.append(adapters_list[-1]+3)

num_ways = [1] + [0]*adapters_list[-1]

for val in adapters_list[1:]:
    num_ways[val] = num_ways[val-1] + num_ways[val-2] + num_ways[val-3]

print(num_ways[adapters_list[-1]])