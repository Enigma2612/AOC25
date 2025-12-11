#New data structure & algorithm encountered: Union Find

with open('8.txt') as f:
    data = f.read()
    coords = [eval(i) for i in data.splitlines()]

def dist2(p1, p2):
    return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2

distances = {}

for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        distances[(i,j)] = dist2(coords[i], coords[j])

sorted_pairs = [(i,j) for i in range(len(coords)) for j in range(i+1, len(coords))]
sorted_pairs.sort(key=lambda x: distances[x])


group_dict = {i:i for i in range(len(coords))}

#finding root / parent of the group of any element
def parent(x):
    if group_dict[x] == x:
        return x
    else:
        root = parent(group_dict[x])        #path contraction
        group_dict[x] = root
        return root

#merging the groups of 2 elements x and y
def merge(x, y):
    group_dict[parent(y)] = parent(x)

for pair in sorted_pairs[:1000]:
    merge(*pair)

grp_sizes = [0]*len(coords)

for i in range(len(coords)):
    grp_sizes[parent(i)] += 1

grp_sizes.sort(key = lambda x: -x)

print(grp_sizes[0]*grp_sizes[1]*grp_sizes[2])


