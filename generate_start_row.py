import numpy

def fill(afnd, height, width):

    start = ['0']

    for c_rows in range(width - 1):
        start.append('')

    afnd = numpy.vstack((afnd, start))

    height += 1

    return afnd, height
