f = open("data/input.txt", "r")
bin_list = f.readlines()

def p1():
    bin_len = len(bin_list)
    running_total = []
    for x in range(len(bin_list[0]) - 1):
        running_total.append(0)
    gamma_rate = ""
    epsilon_rate = ""
    i=0
    for bin in bin_list:
        bin_list[i] = bin.replace('\n','')
        j = 0
        for e in bin_list[i]:
            if e == '1':
                running_total[j]+=1
            j+=1
        i+=1
    k=0
    for t in running_total:
        if (t / bin_len) > 0.5:
            gamma_rate += "1"
            epsilon_rate += "0"
        elif (t / bin_len) < 0.5:
            gamma_rate += "0"
            epsilon_rate += "1"
        k+=1

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"GAMMA: {gamma_rate}, EPSILON: {epsilon_rate}, POWER: {power_consumption}")

p1()

def oxygen_looper(bin_list, x):
    if len(bin_list) > 1:
        new_bin_list = []

        ones_running_sum = 0
        zeros_running_sum = 0

        for item in bin_list:
            if item[x] == '1':
                ones_running_sum+=1
            if item[x] == '0':
                zeros_running_sum+=1

        if ones_running_sum >= zeros_running_sum:
            for item in bin_list:
                if item[x] == '1':
                    new_bin_list.append(item)
        elif zeros_running_sum > ones_running_sum:
            for item in bin_list:
                if item[x] == '0':
                    new_bin_list.append(item)
    else:
        new_bin_list = bin_list
    return new_bin_list

def co2_looper(bin_list, x):
    if len(bin_list) > 1:
        new_bin_list = []

        ones_running_sum = 0
        zeros_running_sum = 0

        for item in bin_list:
            if item[x] == '1':
                ones_running_sum+=1
            if item[x] == '0':
                zeros_running_sum+=1

        if ones_running_sum < zeros_running_sum:
            for item in bin_list:
                if item[x] == '1':
                    new_bin_list.append(item)
        elif zeros_running_sum <= ones_running_sum:
            for item in bin_list:
                if item[x] == '0':
                    new_bin_list.append(item)
    else:
        new_bin_list = bin_list
    return new_bin_list

def p2(bin_list):
    i = 0
    for bin in bin_list:
        bin_list[i] = bin.replace('\n', '')
        i+=1

    o_bin_list = bin_list
    c_bin_list = bin_list

    # oxygen calc
    for x in range(len(o_bin_list[0])):
        o_bin_list = oxygen_looper(o_bin_list, x)

    # CO2 calc
    for x in range(len(c_bin_list[0])):
        c_bin_list = co2_looper(c_bin_list, x)

    print(f"O2: {o_bin_list[0]}, CO2: {c_bin_list[0]}, LIFE SUPPORT RATING: {int(o_bin_list[0],2) * int(c_bin_list[0],2)}")

p2(bin_list)