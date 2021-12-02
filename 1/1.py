import pandas as pd

def read_data():
    data = pd.read_csv('data/input.txt', sep=" ", header=None)
    data.columns = ["val"]
    data['diff'] = None
    return data

def loop(data):
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
i, d = loop(data)
print(f"INCREASED: [{i}], DECREASED: [{d}]")