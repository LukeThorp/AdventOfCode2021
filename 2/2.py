import pandas as pd

def p1():
    df = pd.read_csv("data/input.txt", sep=" ", header=None)
    df.columns = ['dir','dist']

    hor_pos = 0
    depth = 0
    for index, row in df.iterrows():
        if row['dir'] == 'forward':
            hor_pos+=row['dist']
        elif row['dir'] == 'down':
            depth+=row['dist']
        elif row['dir'] == 'up':
            depth-=row['dist']

    final_result = hor_pos*depth

    print(f"Horizontal Pos: {hor_pos}, Depth: {depth}, Final Result: {final_result}")

p1()

def p2():
    df = pd.read_csv("data/input.txt", sep=" ", header=None)
    df.columns = ['dir', 'dist']

    hor_pos = 0
    depth = 0
    aim = 0
    for index, row in df.iterrows():
        if row['dir'] == 'forward':
            hor_pos += row['dist']
            depth += (row['dist']*aim)
        elif row['dir'] == 'down':
            aim += row['dist']
        elif row['dir'] == 'up':
            aim -= row['dist']

    final_result = hor_pos * depth

    print(f"Horizontal Pos: {hor_pos}, Depth: {depth}, Final Result: {final_result}")

p2()