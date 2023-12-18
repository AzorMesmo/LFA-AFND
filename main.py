import numpy


import generate_start_row
import reader
import distinct_tokens
import group_categorizer
import interpreter_words
import interpreter_grammar
import terminal_labels

f_input = open('input.txt', 'r', encoding='utf-8')

# Essential Variables Declaration
# All Variables Starting With "c_" Are Counters (Counters Can Be

groups = [''] * 255
read_state = True
c_groups = 0
afnd = []  # Final Matrix
control_symbols = ['<', '>', '|', ':', '&', '\n']
terminals = []

# Read File And Split In Groups

try:
    while read_state:
        groups[c_groups], read_state = reader.read_file(f_input)
        c_groups += 1
except:
    print('\nERRO: Número Máximo de Grupos Excedido\n')

# Generate A Array With Groups Types (Words Or Grammar)

groups_type = group_categorizer.categorize(groups)

# Generate AFND Horizontal Labels

afnd = distinct_tokens.generate_list(groups, control_symbols, groups_type)

# Store Matrix Size

width = len(afnd)
height = 1

# Generate AFDN Start Row

afnd, height = generate_start_row.fill(afnd, height, width)
afnd[0][0] = ''

# Generate AFND Transitions
for i in range(255 - len(groups_type)):
    groups.remove('')

for group in groups:
    if group[0] == '<':
        afnd, height, width, terminals = interpreter_grammar.fill_matrix(group, afnd, height, width, terminals)
    else:
        afnd, height, width, terminals = interpreter_words.fill_matrix(group, afnd, height, width, terminals)

# Add Terminal Labels

afnd, height = terminal_labels.fill(groups, groups_type, afnd, terminals, height, width)

numpy.savetxt("test.csv", afnd, delimiter=",", fmt="%s")
# https://www.convertcsv.com/csv-viewer-editor.htm


