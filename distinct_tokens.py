def generate_list(groups, symbols, groups_type):
    tokens = []
    c_group = 0
    switch = 0  # Used For Detecting Opening/Closing <>

    for lists in groups:
        for token in lists:
            if groups_type[c_group] == 0:  # Type: Words
                if token not in tokens and token not in symbols:
                    tokens.append(str(token))
            else:  # Type: Grammar
                if token == '<':
                    switch = 1
                if token == '>':
                    switch = 0
                if switch == 0:
                    if token not in tokens and token not in symbols:
                        tokens.append(str(token))
        c_group += 1

    tokens.append('T')

    tokens.insert(0, '''
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
    ''')  # First Element Empty For Table Integrity (Big For Python Do Not Cut The Elements In Matrix)

    return tokens
