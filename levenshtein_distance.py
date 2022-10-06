import logging

def lev_dis(s1, s2):
    if s1 == s2:
        return 0;
    s1_arr = s1.split()
    s2_arr = s2.split()
    s1_len = len(s1_arr)
    s2_len = len(s2_arr)
    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len
    # create a s1_len x s2_len matrix that stores each score
    matrix = [[] for i in range(s1_len + 1)]
    for i in range(s1_len + 1):
        matrix[i] = [0 for j in range(s2_len + 1)]
    
    for i in range(s1_len + 1):
        matrix[i][0] = i
    for j in range(s2_len + 1):
        matrix[0][j] = j

    for i in range(1, s1_len + 1):
        s1_word = s1_arr[i-1]
        for j in range(1, s2_len + 1):
            s2_word = s2_arr[j-1]
            cost = 0 if (s1_word == s2_word) else 1
            matrix[i][j] = min([matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost])
    
    return matrix[s1_len][s2_len]

def word_error_rate(text, error):
    return error/len(text.split())


s1 = input('Enter Reference Sentence: ')
s2 = input('Enter Hypothesis Sentence: ')
ld = lev_dis(s1, s2)
wer = word_error_rate(s1, ld) * 100
print(f"The Levenshtein Distance (number of errors): {ld}")
print(f"The Word Error Rate(WER): {round(wer, 2)}%")
