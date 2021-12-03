# Part 1: What is the power consumption of the submarine? [ 1092896 ]

with open('3_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]

gamma_rate = ''
epsilon_rate = ''

def binary_to_decimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        decimal = decimal + (binary % 10) * pow(2, i)
        binary //= 10
        i += 1
    return decimal

for c in range(len(data_list[0])):
    zeros = 0
    ones = 0
    for r in range(len(data_list)):
        if (data_list[r][c] == '0'):
            zeros += 1
        else:
            ones += 1
    if (zeros > ones):
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(binary_to_decimal(int(gamma_rate)) * binary_to_decimal(int(epsilon_rate)))