import generate_row


def fill_matrix(group, afnd, height, width, terminals):
    reader = ''
    e_list = []
    dic = {}
    c_main = 0
    first = True
    terminal = False
    current = 0

    while c_main < len(group):
        while group[c_main] != '\n':
            if group[c_main] == '<' or group[c_main] == '>':
                e_list.append(str(reader))
                reader = ''
            elif group[c_main] == '|' or group[c_main] == ':':
                pass
            elif group[c_main] == '&':
                terminal = True
            else:
                reader += str(group[c_main])
            c_main += 1
        if c_main != len(group):
            c_main += 1

        e_list.pop(0)
        if first:
            dic[e_list[0]] = str(1)
            first = False
        current = dic.get(e_list[0])
        e_list.pop(0)

        switch = True

        for writer in e_list:
            if switch:
                pass
                switch = False
            else:
                try:
                    placeholder = dic[str(writer)]
                except:
                    afnd, height = generate_row.add(afnd, height, width)
                    dic[str(writer)] = height - 1
                switch = True

        switch = True
        pos_token = 0

        for writer in e_list:
                if switch:
                    # Get The Column(s) Of The Token (pos_token)
                    pos_counter = 0
                    for counter in range(width):
                        if writer == afnd[0][counter]:
                            pos_token = str(pos_counter)
                        pos_counter += 1
                    switch = False
                else:
                    if afnd[int(current)][int(pos_token)] == '':
                        afnd[int(current)][int(pos_token)] = str(int(dic.get(writer)) - 1)
                    else:
                        afnd[int(current)][int(pos_token)] = '|' + str(int(dic.get(writer)) - 1)
                    switch = True

        if terminal:
            afnd[int(current)][0] += '*'
            terminals.append(current)

        e_list = []

    return afnd, height, width, terminals
