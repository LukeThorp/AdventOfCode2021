import pandas as pd
import sys

f = open("data/input.txt", "r")
input_list = f.readlines()

def get_number_order(input_list, board_size):

    number_list = input_list[0]

    number_list = number_list.replace('\n','').split(',')

    i=0
    for number in number_list:
        number_list[i] = int(number)
        i+=1

    boards = []

    input_list = input_list[1:]
    output_list = []

    for ele in input_list:
        if ele == '\n':
            pass
        else:
            ele = ele.replace('\n', '')
            ele = ele.replace('  ', ' ')
            if ele.startswith(' '):
                ele = ele[1:]
            output_list.append(ele)

    board_count = len(output_list) / board_size

    j = 0
    j_end = board_size-1
    for x in range(int(board_count)):
        board_n = [output_list[j:j_end+1]]
        j+=board_size
        j_end+=board_size
        boards.append(board_n)

    return boards, number_list

def board_checker(boards, number_list, board_size):

    boards_final = []

    i=0
    j=0
    k=0
    for board in boards:
        board_final = []

        for r in range(board_size):
            row = board[0][r].split(' ')
            row_parsed = []
            for ele in row:
                row_parsed.append(int(ele))
            board_final.append(row_parsed)

        boards_final.append(board_final)


    boards_final_copy = boards_final

    i=0
    j=0
    k=0
    for number in number_list:
        print(f"CHECKING NUMBER: {number} - {k+1}/{len(number_list)}")
        for board in boards_final:
            for row in board:
                row = [-1 if x==number else x for x in row]
                try:
                    boards_final[i][j] = row
                except IndexError:
                    print(i,j,boards_final)
                    print(row)
                    sys.exit()
                boards_final = checker(boards_final, boards, number)
                j+=1
                if j==board_size:
                    j = 0
            i+=1
        k+=1
        i=0
        j=0


def final_sum(board, number):
    running_sum = 0
    for row in board:
        for ele in row:
            if ele == -1:
                pass
            else:
                running_sum += ele
    print(running_sum * number)


def checker(boards_final, boards, number):
    k=0
    for board in boards_final:

        # hor check
        for row in board:
            if sum(row) == -5:
                print(f"BINGO - BOARD:{k}")
                final_sum(board, number)
                print(boards[k])
                sys.exit()
        # vert check
        running_count = 0
        for vert in range(board_size):
            for row in board:
                running_count+=int(row[vert])
            if running_count > -5:
                running_count = 0
            else:
                print(f"BINGO - BOARD:{k}")
                final_sum(board, number)
                print(boards[k])
                sys.exit()
        # diag check
        i = 0
        running_count = 0
        for board in boards_final:
            for row in board:
                running_count+=int(row[i])
                i+=1
            if running_count > -5:
                running_count = 0
            else:
                print(f"BINGO - BOARD:{k}")
                final_sum(board, number)
                print(boards[k])
                sys.exit()
            i = 0
        i = board_size-1
        running_count = 0
        for board in boards_final:
            for row in board:
                running_count += int(row[i])
                i -= 1
            if running_count > -5:
                running_count = 0
            else:
                print(f"BINGO - BOARD:{k}")
                final_sum(board, number)
                print(boards[k])
                sys.exit()
            i = 0
        k+=1
    return boards_final




board_size = 5
boards, number_list = get_number_order(input_list, board_size)

board_checker(boards, number_list, board_size)