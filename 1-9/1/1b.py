# Part 2: How many sums are larger than the previous sum? [ x ]

data = open("1_data.txt", "r")
data_list = data.readlines()
prev_sum = 0
total_increased = -1

for i in range(len(data_list) - 2):
    if (int(data_list[i]) + int(data_list[i+1]) + int(data_list[i+2]) > prev_sum):
        total_increased += 1
    prev_sum = int(data_list[i]) + int(data_list[i+1]) + int(data_list[i+2])

print(total_increased)
