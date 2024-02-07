import string

# input example
sentence = input('Masukkan kalimat: ')
input_string = sentence.lower()+'#'

# initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0','q1','q2','q3','q4','q5','q6','q7','q8', 'q9', 'q10',
              'q11','q12','q13','q14','q15','q16','q17','q18', 'q19', 'q20', 
              'q21','q22','q23','q24','q25','q26','q27','q28', 'q29', 'q30',
              'q31','q32','q33','q34','q35','q36','q37','q38', 'q39', 'q40', 'q41', 'q42']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# spaces before input string
transition_table['q0', ' '] = 'q0'

# update the transition table for the following token: abdi
transition_table[('q0', 'a')] = 'q1'
transition_table[('q1', 'b')] = 'q2'
transition_table[('q2', 'd')] = 'q3'
transition_table[('q3', 'i')] = 'q4'
transition_table[('q4', ' ')] = 'q41'
transition_table[('q4', '#')] = 'accept'

# update the transition table for the following token: bapa
transition_table[('q0', 'b')] = 'q5'
transition_table[('q5', 'a')] = 'q6'
transition_table[('q6', 'p')] = 'q7'
transition_table[('q7', 'a')] = 'q8'
transition_table[('q8', ' ')] = 'q41'
transition_table[('q8', '#')] = 'accept'

# update the transition table for the following token: indung
transition_table[('q0', 'i')] = 'q9'
transition_table[('q9', 'n')] = 'q10'
transition_table[('q10', 'd')] = 'q11'
transition_table[('q11', 'u')] = 'q12'
transition_table[('q12', 'n')] = 'q13'
transition_table[('q13', 'g')] = 'q14'
transition_table[('q14', ' ')] = 'q41'
transition_table[('q14', '#')] = 'accept'

# update the transition table for the following token: bal
transition_table[('q0', 'b')] = 'q5'
transition_table[('q5', 'a')] = 'q6'
transition_table[('q6', 'l')] = 'q42'
transition_table[('q42', ' ')] = 'q41'
transition_table[('q42', '#')] = 'accept'

# update the transition table for the following token: sayur
transition_table[('q0', 's')] = 'q15'
transition_table[('q15', 'a')] = 'q16'
transition_table[('q16', 'y')] = 'q17'
transition_table[('q17', 'u')] = 'q18'
transition_table[('q18', 'r')] = 'q19'
transition_table[('q19', ' ')] = 'q41'
transition_table[('q19', '#')] = 'accept'

# update the transition table for the following token: acuk
transition_table[('q0', 'a')] = 'q1'
transition_table[('q1', 'c')] = 'q20'
transition_table[('q20', 'u')] = 'q35'
transition_table[('q35', 'k')] = 'q36'
transition_table[('q36', ' ')] = 'q41'
transition_table[('q36', '#')] = 'accept'

# update the transition table for the following token: runtah
transition_table[('q0', 'r')] = 'q21'
transition_table[('q21', 'u')] = 'q22'
transition_table[('q22', 'n')] = 'q23'
transition_table[('q23', 't')] = 'q24'
transition_table[('q24', 'a')] = 'q25'
transition_table[('q25', 'h')] = 'q26'
transition_table[('q26', ' ')] = 'q41'
transition_table[('q26', '#')] = 'accept'

# update the transition table for the following token: miceun
transition_table[('q0', 'm')] = 'q27'
transition_table[('q27', 'i')] = 'q28'
transition_table[('q28', 'c')] = 'q29'
transition_table[('q29', 'e')] = 'q30'
transition_table[('q30', 'u')] = 'q31'
transition_table[('q31', 'n')] = 'q32'
transition_table[('q32', ' ')] = 'q41'
transition_table[('q32', '#')] = 'accept'

# update the transition table for the following token: masak
transition_table[('q0', 'm')] = 'q27'
transition_table[('q27', 'a')] = 'q33'
transition_table[('q33', 's')] = 'q34'
transition_table[('q34', 'a')] = 'q35'
transition_table[('q35', 'k')] = 'q36'
transition_table[('q36', ' ')] = 'q41'
transition_table[('q36', '#')] = 'accept'

# update the transition table for the following token: nyandak
transition_table[('q0', 'n')] = 'q37'
transition_table[('q37', 'y')] = 'q38'
transition_table[('q38', 'a')] = 'q39'
transition_table[('q39', 'n')] = 'q40'
transition_table[('q40', 'd')] = 'q34'
transition_table[('q34', 'a')] = 'q35'
transition_table[('q35', 'k')] = 'q36'
transition_table[('q36', ' ')] = 'q41'
transition_table[('q36', '#')] = 'accept'

# update the transition table for state q41
transition_table[('q41', ' ')] = 'q41'
transition_table[('q41', '#')] = 'accept'

# transition for new tokens
transition_table[('q41', 'n')] = 'q37'
transition_table[('q41', 'm')] = 'q27'
transition_table[('q41', 'a')] = 'q1'
transition_table[('q41', 'b')] = 'q5'
transition_table[('q41', 'i')] = 'q9'
transition_table[('q41', 's')] = 'q15'
transition_table[('q41', 'r')] = 'q21'

tokens = sentence.lower().split()
tokens.append('EOS')

# symbols definition
non_terminals = ['S', 'NN', 'VB']
terminals = ['abdi', 'bapa', 'indung', 'bal', 'sayur', 'acuk', 'runtah', 'miceun', 'masak', 'nyandak']

# parse table definition
parse_table = {}

parse_table[('S', 'abdi')] = ['NN', 'VB', 'NN']
parse_table[('S', 'bapa')] = ['NN', 'VB', 'NN']
parse_table[('S', 'indung')] = ['NN', 'VB', 'NN']
parse_table[('S', 'bal')] = ['NN', 'VB', 'NN']
parse_table[('S', 'sayur')] = ['NN', 'VB', 'NN']
parse_table[('S', 'acuk')] = ['NN', 'VB', 'NN']
parse_table[('S', 'runtah')] = ['NN', 'VB', 'NN']
parse_table[('S', 'miceun')] = ['error']
parse_table[('S', 'masak')] = ['error']
parse_table[('S', 'nyandak')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'abdi')] = ['abdi']
parse_table[('NN', 'bapa')] = ['bapa']
parse_table[('NN', 'indung')] = ['indung']
parse_table[('NN', 'bal')] = ['bal']
parse_table[('NN', 'sayur')] = ['sayur']
parse_table[('NN', 'acuk')] = ['acuk']
parse_table[('NN', 'runtah')] = ['runtah']
parse_table[('NN', 'miceun')] = ['error']
parse_table[('NN', 'masak')] = ['error']
parse_table[('NN', 'nyandak')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'abdi')] = ['error']
parse_table[('VB', 'bapa')] = ['error']
parse_table[('VB', 'indung')] = ['error']
parse_table[('VB', 'bal')] = ['error']
parse_table[('VB', 'sayur')] = ['error']
parse_table[('VB', 'acuk')] = ['error']
parse_table[('VB', 'runtah')] = ['error']
parse_table[('VB', 'miceun')] = ['miceun']
parse_table[('VB', 'masak')] = ['masak']
parse_table[('VB', 'nyandak')] = ['nyandak']
parse_table[('VB', 'EOS')] = ['error']

# lexical analysis
valid = False
idx_char = 0
state = 'q0'
current_token = ''
while state !='accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state == 'error':
        print('error')
        break
    idx_char += 1
# conclusion
print('Hasil Lexical Analyzer:')
if state=='accept':
  valid = True
  print('Semua token di input: ', sentence, ', valid')
else:
  print('Semua token di input: ', sentence, ', tidak valid. Program parser tidak akan berjalan.')

if valid:
  print()
  print('Hasil Parser:')
  print()
  # stack initialization
  stack = []
  stack.append('#')
  stack.append('S')
  # input reading initialization
  idx_token = 0
  symbol = tokens[idx_token]
  # parsing process
  while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top =', top)
    print('symbol =', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token += 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack:', stack)
                stack.pop()
        else:
            print('error')
            break
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break
    else:
        print('error')
        break
    print('isi stack:', stack)
    print()
  # conclusion
  if symbol == 'EOS' and len(stack) == 0:
    print('Input string: ', sentence, ', diterima, sesuai Grammar',sep='')
  else:
    print('Input string: ', sentence, ', tidak diterima, tidak sesuai Grammar',sep='')