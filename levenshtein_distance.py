def levenshtein_distance(s1, s2):
    """Compute the Levenshtein distance between two strings."""
    s1_arr = s1.split()
    s2_arr = s2.split()
    s1_len = len(s1_arr)
    s2_len = len(s2_arr)

    matrix = [[0 for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]
    arrow_matrix = [[" " for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]

    for i in range(s1_len + 1):
        matrix[i][0] = i
    for j in range(s2_len + 1):
        matrix[0][j] = j

    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            cost = 0 if s1_arr[i-1] == s2_arr[j-1] else 1
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)
            
            if matrix[i-1][j] + 1 < matrix[i][j-1] + 1 and matrix[i-1][j] + 1 < matrix[i-1][j-1] + cost:
                arrow_matrix[i][j] = "↑"
            elif matrix[i][j-1] + 1 < matrix[i-1][j] + 1 and matrix[i][j-1] + 1 < matrix[i-1][j-1] + cost:
                arrow_matrix[i][j] = "←"
            elif cost == 1:
                arrow_matrix[i][j] = "↖"
            else:
                arrow_matrix[i][j] = "x"

    return matrix[s1_len][s2_len], arrow_matrix

def count_error(arrow_matrix, i, j):
    """Count the substitution, deletion, and insertion errors based on the arrow matrix."""
    sub_count, del_count, ins_count = 0, 0, 0
    
    if i == 0:
        return 0, 0, j
    if j == 0:
        return 0, i, 0
    
    if arrow_matrix[i][j] == "x":
        return count_error(arrow_matrix, i-1, j-1)
    elif arrow_matrix[i][j] == "↖":
        sub_count += 1
        sub, delete, insert = count_error(arrow_matrix, i-1, j-1)
        return sub_count + sub, delete, insert
    elif arrow_matrix[i][j] == "↑":
        del_count += 1
        sub, delete, insert = count_error(arrow_matrix, i-1, j)
        return sub, del_count + delete, insert
    elif arrow_matrix[i][j] == "←":
        ins_count += 1
        sub, delete, insert = count_error(arrow_matrix, i, j-1)
        return sub, delete, ins_count + insert
    else:
        return 0, 0, 0

def word_error_rate(text, error):
    """Calculate word error rate."""
    text_length = len(text.split())
    if text_length > 0:
        return error / text_length
    else:
        return -1

def lev_dis(s1, s2):
    ld, arrow_matrix = levenshtein_distance(s1, s2)
    sub_count, del_count, ins_count = count_error(arrow_matrix, len(s1.split()), len(s2.split()))
    return ld, sub_count, del_count, ins_count
