import logging

sub_count = 0
del_count = 0
ins_count = 0
arrow_matrix = [[]]

def lev_dis(s1, s2):
    global sub_count, del_count, ins_count
    global arrow_matrix

    # initialize 
    sub_count = 0
    del_count = 0
    ins_count = 0

    s1_arr = s1.split()
    s2_arr = s2.split()
    s1_len = len(s1_arr)
    s2_len = len(s2_arr)

    # create a s1_len x s2_len matrix that stores each score
    matrix = [[] for i in range(s1_len + 1)]
    arrow_matrix = [[] for i in range(s1_len + 1)]

    for i in range(s1_len + 1):
        matrix[i] = [0 for j in range(s2_len + 1)]
        arrow_matrix[i] = [" " for j in range(s2_len + 1)]

    for i in range(s1_len + 1):
        matrix[i][0] = i
    for j in range(s2_len + 1):
        matrix[0][j] = j

    if s1 == s2:
        return 0
    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len

    for i in range(1, s1_len + 1):
        s1_word = s1_arr[i-1]
        for j in range(1, s2_len + 1):
            s2_word = s2_arr[j-1]
            cost = 0 if (s1_word == s2_word) else 1
            if matrix[i-1][j] + 1 <  matrix[i][j-1] + 1 and matrix[i-1][j] + 1 < matrix[i-1][j-1] + cost:
                arrow_matrix[i][j] = "↑"
            elif matrix[i][j-1] + 1 < matrix[i-1][j] + 1 and matrix[i][j-1] + 1 < matrix[i-1][j-1] + cost:
                arrow_matrix[i][j] = "←"
            elif cost == 1:
                arrow_matrix[i][j] = "↖"
            else:
                arrow_matrix[i][j] = "x"

            matrix[i][j] = min([matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost])

    for i in range(s1_len + 1):
        print(arrow_matrix[i])
    for i in range(s1_len + 1):
        print(matrix[i])
    
    return matrix[s1_len][s2_len]

def count_error(i, j):

    global sub_count, del_count, ins_count
    if i == 0 and j ==0:
        return 'Done'
    elif j == 0:
        del_count = del_count + i
        return 'Done'
    elif i == 0:
        ins_count = ins_count + j
        return 'Done'
    
    if arrow_matrix[i][j] == "x":
        count_error(i-1, j-1)
    elif arrow_matrix[i][j] == "↖":
        sub_count = sub_count + 1
        count_error(i-1, j-1)
    elif arrow_matrix[i][j] == "↑":
        del_count = del_count + 1
        count_error(i-1, j)
    elif arrow_matrix[i][j] == "←":
        ins_count = ins_count + 1
        count_error(i, j-1)
    else:
        logging.error('Unknown character is in the table')
        return 'Error'

def word_error_rate(text, error):
    if (len(text) > 0):
        return error/len(text.split())
    else:
        return -1

# ------------------------ Test in the terminal ------------------------
s1 = input('Enter Reference Sentence: ')
s2 = input('Enter Hypothesis Sentence: ')
s1_arr = s1.split()
s2_arr = s2.split()
s1_len = len(s1_arr)
s2_len = len(s2_arr)
ld = lev_dis(s1, s2)
wer = word_error_rate(s1, ld) * 100

print(f"The Levenshtein Distance (number of errors): {ld}")
print(f"The Word Error Rate(WER): {round(wer, 2)}%")

count_error(s1_len, s2_len)
print(f"Sub: {sub_count}. Del: {del_count}. Ins: {ins_count}")
