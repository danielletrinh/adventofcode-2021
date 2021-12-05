# Part 2: Once it wins, what would its final score be? [ WIP ]

with open('4_data.txt', 'rt') as data:
    draw_list = data.readline().split(',')
    data.readline()
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split()

boards = [[0]]

def check_boards():
    for i in range(1, len(boards)):
        for r in range(int(boards[i][0]), int(boards[i][1])):
            streak = 0
            for c in range(len(data_list[r])):
                if data_list[r][c] == '':
                    streak += 1
            if streak == 5:
                result = True, int(boards[i][0]), int(boards[i][1])
                del boards[i]
                return result

        for c in range(len(data_list[0])):
            streak = 0
            for r in range(int(boards[i][0]), int(boards[i][1])):
                if data_list[r][c] == '':
                    streak += 1
            if streak == 5:
                result = True, int(boards[i][0]), int(boards[i][1])
                del boards[i]
                return result

    return False, False, False

def run():
    for r in range(len(data_list)):
        if len(data_list[r]) < 2:
            boards.append([boards[-1][0] + 1, r])
    del boards[0]
    boards_left = len(boards)

    for i in range(len(draw_list)):
        for r in range(len(data_list)):
            for c in range(len(data_list[r])):
                if data_list[r][c] == draw_list[i]:
                    data_list[r][c] = ''
                    complete, board_start, board_finish = check_boards()
                    if complete:
                        boards_left -= 1
                        if len(boards) == 1:
                            sum = 0
                            for row in range(board_start, board_finish):
                                for col in range(len(data_list[row])):
                                    if data_list[row][col] != '':
                                        sum += int(data_list[row][col])
                            return sum * int(draw_list[i])

print(run())