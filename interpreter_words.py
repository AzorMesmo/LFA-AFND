import generate_row


def fill_matrix(group, afnd, height, width, terminals):
    depth = 1
    skip = False
    for token in range(len(group)):

        if not skip:  # Used To Skip \n Tokens

            # Get The Column(s) Of The Token (pos_token)
            pos_label = 0
            for label in afnd[0]:
                if group[token] == label:
                    pos_token = str(pos_label)
                pos_label += 1

            if group[token + 1] != '\n':
                # Get Token Transition Column (pos_next)
                pos_label = 0
                for label in afnd[0]:
                    if group[token + 1] == label:
                        pos_next = pos_label
                    pos_label += 1
            else:
                pos_next = False

            # Verify If The Transition Already Exists
            if afnd[depth][int(pos_token)] != '':  # token > Exist
                if not pos_next:  # pos_next = \n
                    depth_before = depth
                    afnd, height = generate_row.add(afnd, height, width)
                    depth = height - 2
                    afnd[depth_before][int(pos_token)] = afnd[depth_before][int(pos_token)] + '|' + str(depth)
                    afnd[depth][0] = afnd[depth][0] + '*'
                    terminals.append(depth)
                    depth = 1
                    skip = True
                else:
                    transitions = list(afnd[depth][int(pos_token)])
                    for label in transitions:  # Multiple Transitions Matter (So We Do All)
                        if label != '|':
                            if afnd[int(label) + 1][int(pos_next)] == '':  # next > Not Exist
                                new_row = True
                            else:  # next = Exist
                                depth += 1
                                new_row = False
                                break
                    if new_row:
                        depth_before = depth
                        afnd, height = generate_row.add(afnd, height, width)
                        depth = height - 2
                        afnd[depth_before][int(pos_token)] = (afnd[depth_before][int(pos_token)] + '|' + str(depth))
                        depth += 1
            else:  # token = Not Exist
                depth_before = depth
                afnd, height = generate_row.add(afnd, height, width)
                depth = height - 2
                afnd[depth_before][int(pos_token)] = str(depth)
                depth += 1
                if not pos_next:  # pos_next = \n
                    afnd[depth][0] = afnd[depth][0] + '*'
                    terminals.append(depth)
                    depth = 1
                    skip = True
        else:
            skip = False

    return afnd, height, width, terminals
