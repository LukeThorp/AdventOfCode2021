import pandas as pd

def read_data():
    data = pd.read_csv('data/part 1/input.txt', sep=" ", header=None)
    data.columns = ["val"]
    data['diff'] = None
    return data

def p1_loop(data):
    increased = 0
    decreased = 0
    current_val = "NA"
    for index, row in data.iterrows():
        if current_val == "NA":
            pass
        elif current_val < row['val']:
            increased+=1
        else:
            decreased += 1
        current_val = data.iloc[index]["val"]
    return increased, decreased

data = read_data()
i, d = p1_loop(data)
print(f"PART 1: INCREASED: [{i}], DECREASED: [{d}]")


def organise_data():
    val_list = data['val'].to_list()
    return val_list

def p2_loop(val_list):
    increased = 0
    decreased = 0
    nochange = 0
    current_val = "NA"
    for i in range(len(val_list)-2):
        if current_val == "NA":
            pass
        elif current_val < val_list[i] + val_list[i+1] + val_list[i+2]:
            increased+=1
        elif current_val == val_list[i] + val_list[i+1] + val_list[i+2]:
            nochange+=1
        else:
            decreased+=1
        current_val = val_list[i] + val_list[i + 1] + val_list[i + 2]
    return increased, decreased, nochange

val_list = organise_data()
i,d,n = p2_loop(val_list)
print(f"PART 2: INCREASED: [{i}], DECREASED: [{d}], NOCHANGE: [{d}]")
