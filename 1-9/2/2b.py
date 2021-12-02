# Part 2: What do you get if you multiply your final horizontal position by your final depth? [ 1845455714 ]

with open("2_data.txt", "rt") as data:
    data_list = [line.strip() for line in data.readlines()]

horizontal_position = 0
depth = 0
aim = 0

for i in range(len(data_list)):
    direction, steps = data_list[i].split()
    if (direction == "forward"):
        horizontal_position += int(steps)
        depth += (aim * int(steps))
    elif (direction == "down"):
        aim += int(steps)
    elif (direction == "up"):
        aim -= int(steps)

print(horizontal_position * depth)