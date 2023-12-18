import generate_row


def fill(groups, groups_type, afnd, terminals, height, width):
    reader = ''
    storage = []

    for counter in range(len(groups_type)):
        if not groups_type[counter]:  # Words
            for token in groups[counter]:
                if token != '\n':
                    reader += token
                else:
                    storage.append(reader)
                    reader = ''
        else:  # Grammar
            pass

    extra = 0
    for counter in terminals:
        if extra < len(storage):
            afnd[counter][-1] = storage[extra]
        else:
            afnd[counter][-1] = 'var'
        extra += 1

    afnd, height = generate_row.add(afnd, height, width)

    for i in range(height):
        for j in range(width - 1):
            if afnd[i][j] == '':
                afnd[i][j] = str(height - 2)

    afnd[0][0] = ''

    return afnd, height
