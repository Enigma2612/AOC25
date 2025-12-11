with open("9.txt") as f:
    data = f.read()

coords = [eval(i) for i in data.splitlines()]

def area(a,b):
    return ((b[1]-a[1]+1)*(b[0]-a[0]+1))

max_area = 0

for i in range(len(coords)):
    for j in range(len(coords)):
        max_area = max(area(coords[i],coords[j]), max_area)

print(max_area)