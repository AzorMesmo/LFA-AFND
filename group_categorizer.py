def categorize(groups):
    groups_type = []

    for lists in groups:
        for token in lists:
            if token == '<':
                groups_type.append(1)
                break
            else:
                groups_type.append(0)
                break

    return groups_type
