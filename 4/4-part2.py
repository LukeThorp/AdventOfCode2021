import pandas as pd
import sys

f = open("data/test.txt", "r")
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

    board_status = []
    for x in range(len(boards)):
        board_status.append(False)

    return boards, number_list, board_status

def board_checker(boards, number_list, board_size, board_status):

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
    final_cwb = None
    final_cwn = None
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
                    continue
                boards_final, current_winning_board, current_winning_number = checker(boards_final, boards, number, board_status)
                if current_winning_board != None:
                    final_cwb = current_winning_board
                    if current_winning_number != None:
                        final_cwn = current_winning_number
                    break
                current_winning_number = None
                current_winning_board = None
                j+=1
                if j==board_size:
                    j = 0
            i+=1
        k+=1
        i=0
        j=0

        print("current_win_num:", final_cwn)
        print("current_win_board:", final_cwb)
    final_sum(current_winning_board, number)


def final_sum(board, number):

    
    running_sum = 0
    for row in board:
        for ele in row:
            if ele == -1:
                pass
            else:
                running_sum += ele
    print(f"Final Result: {running_sum * number}")


def checker(boards_final, boards, number, board_status):

    k=0
    current_winning_board = None
    current_winning_number = None
    for board in boards_final:
        if board_status[k] == False:
            # hor check
            for row in board:
                if sum(row) == -5:
                    current_winning_board = board
                    current_winning_number = number
                    print(f"BOARD MARKED {k} - {number}")
                    board_status[k] = True
                    break
            # vert check
            running_count = 0
            for vert in range(board_size):
                for row in board:
                    running_count+=int(row[vert])
                if running_count > -5:
                    running_count = 0
                else:
                    current_winning_board = board
                    current_winning_number = number
                    print(f"BOARD MARKED {k} - {number}")
                    board_status[k] = True
                    break
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
                    current_winning_board = board
                    current_winning_number = number
                    print(f"BOARD MARKED {k} - {number}")
                    board_status[k] = True
                    break
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
                    current_winning_board = board
                    current_winning_number = number
                    print(f"BOARD MARKED {k} - {number}")
                    board_status[k] = True
                    break
                i = 0
        if current_winning_number != None and current_winning_board != None:
            continue
        k+=1
    return boards_final, current_winning_board, current_winning_number




board_size = 5
boards, number_list, board_status = get_number_order(input_list, board_size)

board_checker(boards, number_list, board_size, board_status)