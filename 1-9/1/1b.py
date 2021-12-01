# Part 2: How many sums are larger than the previous sum? [ x ]

data = open("1_data.txt", "r")
data_list = data.readlines()
prev_sum = 0
total_increased = -1

for i in range(len(data_list) - 2):
    n1, n2, n3 = int(data_list[i]), int(data_list[i+1]), int(data_list[i+2])
    increased = (n1 + n2 + n3) > prev_sum
    if (increased):
        total_increased += 1
    prev_sum = n1 + n2 + n3

print(total_increased)
