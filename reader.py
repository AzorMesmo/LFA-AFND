# Return Dictionary
# 0 > End Of File
# 1 > End Of Group


def read_file(f_input):
    # Counters
    c_linebreaks = 0  # Count Line Breaks

    # Final Group
    group = []

    while True:
        reader = f_input.read(1)
        if not reader:
            return group, False
        elif reader == '\n':
            c_linebreaks += 1
            if c_linebreaks == 2:
                return group, True
            group.append(reader)
        else:
            group.append(reader)
            c_linebreaks = 0