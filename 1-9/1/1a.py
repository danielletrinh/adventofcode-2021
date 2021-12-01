# Part 1: How many measurements are larger than the previous measurement? [ 1616 ]

data = open("1_data.txt", "r")
data_list = data.readlines()
total_increased = 0

for i in range(len(data_list) - 1):
    if (int(data_list[i+1]) > int(data_list[i])):
        total_increased += 1

print(total_increased)
