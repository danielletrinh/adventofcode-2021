# Part 1: What will your final score be if you choose that board? [ 58838 ]

with open('4_data.txt', 'rt') as data:
    draw_list = data.readline().split(',')
    data.readline()
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split()

boards = [0]

def check_boards():
    for i in range(1, len(boards)):
        for r in range(int(boards[i-1]) + 1, int(boards[i])):
            streak = 0
            for c in range(len(data_list[r])):
                if data_list[r][c] == '':
                    streak += 1
            if streak == 5:
                return True, int(boards[i-1]) + 1, int(boards[i])

        for c in range(len(data_list[0])):
            streak = 0
            for r in range(int(boards[i-1]) + 1, int(boards[i])):
                if data_list[r][c] == '':
                    streak += 1
            if streak == 5:
                return True, int(boards[i-1]) + 1, int(boards[i])

    return False, False, False

def run():
    for i in range(len(draw_list)):
        for r in range(len(data_list)):
            if len(data_list[r]) < 1:
                boards.append(r)
            for c in range(len(data_list[r])):
                if data_list[r][c] == draw_list[i]:
                    data_list[r][c] = ''
                    complete, board_start, board_finish = check_boards()
                    if (complete):
                        sum = 0
                        for row in range(board_start, board_finish):
                            for col in range(len(data_list[row])):
                                if data_list[row][col] != '':
                                    sum += int(data_list[row][col])
                        return sum * int(draw_list[i])

print(run())