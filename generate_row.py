import numpy


def add(afnd, height, width):
    new_row = [str(height - 1)]

    height += 1

    for c_rows in range(width - 1):
        new_row.append('')

    afnd = numpy.vstack((afnd, new_row))

    return afnd, height
