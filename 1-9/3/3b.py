# Part 2: What is the life support rating of the submarine? [ 4672151 ]

with open('3_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]

def binary_to_decimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        decimal = decimal + (binary % 10) * pow(2, i)
        binary //= 10
        i += 1
    return decimal

def find_rating(bit):
    new_data_list = data_list.copy()
    for c in range(len(new_data_list[0])):
        zeros = 0
        ones = 0
        for r in range(len(new_data_list)):
            if (new_data_list[r][c] == '0'):
                zeros += 1
            else:
                ones += 1

        if (zeros > ones):
            greater = '0'
        elif (ones > zeros):
            greater = '1'
        else:
            greater = -1

        if (bit == 1):
            if (greater == -1):
                newer_data_list = [x for x in new_data_list if x[c] == '1']
            else:
                newer_data_list = [x for x in new_data_list if x[c] == greater]
        else:
            if (greater == -1):
                newer_data_list = [x for x in new_data_list if x[c] == '0']
            else:
                newer_data_list = [x for x in new_data_list if x[c] != greater]
        new_data_list = newer_data_list.copy()
        if (len(newer_data_list) == 1):
            return newer_data_list[0]

print(binary_to_decimal(int(find_rating(0))) * binary_to_decimal(int(find_rating(1))))