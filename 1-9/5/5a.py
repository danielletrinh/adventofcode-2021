# Part 1: At how many points do at least two lines overlap? [ 7674 ]

with open('5_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split(' -> ')

grid = [[0 for i in range(1000)] for j in range(1000)]
overlapping = 0

def add_points(line):
    x1, y1 = line[0].split(',')
    x2, y2 = line[1].split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    if x1 == x2:
        if y2 > y1:
            while y2 >= y1:
                grid[x1][y1] += 1
                y1 += 1
        elif y2 < y1:
            while y2 <= y1:
                grid[x1][y1] += 1
                y1 -= 1
    elif y1 == y2:
        if x2 > x1:
            while x2 >= x1:
                grid[x1][y1] += 1
                x1 += 1
        elif x2 < x1:
            while x2 <= x1:
                grid[x1][y1] += 1
                x1 -= 1

for line in data_list:
    add_points(line)

for row in grid:
    for item in row:
        if item >= 2: overlapping += 1

print(overlapping)
