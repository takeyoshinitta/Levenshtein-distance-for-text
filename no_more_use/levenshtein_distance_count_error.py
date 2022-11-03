# Below are the costs of different operations.
ins_cost = 1
del_cost = 1
sub_cost = 1

# Below function will take the two sequence and will return the distance between them.
def edit_distance_recurse(s1_arr, s2_arr, operations = []):
    """Returns the Edit Distance between the provided two sequences."""

    global count_ins, count_del, count_sub
    
    if len(s2_arr) == 0:
        operations = operations + ([f"Delete `{s1_arr}` from sequence1."] if len(s1_arr) else [])
        return len(s1_arr), operations
    
    if len(s1_arr) == 0:
        operations = operations + ([f"Insert `{s2_arr}` into sequence1."] if len(s2_arr) else [])
        return len(s2), operations
    
    if s1_arr[0] == s2_arr[0]:
        operations = operations + [f"Make no change for word `{s1_arr[0]}`."]
        return edit_distance_recurse(s1_arr[1: ], s2_arr[1: ], operations)
    
    # calculate cost if insertion was made
    ins_operations = operations + [f"Insert `{s2_arr[0]}` in sequence1."]
    insertion, ins_operations = edit_distance_recurse(s1_arr, s2_arr[1: ], ins_operations)
    
    # calculate cost if deletion was done
    del_operations = operations + [f"Delete `{s1_arr[0]}` from sequence1."]
    deletion, del_operations = edit_distance_recurse(s1_arr[1: ], s2_arr, del_operations)
    
    # calculate cost if substitution was done
    sub_operations = operations + [f"Substitute `{s1_arr[0]}` in sequence1 with `{s2_arr[0]}`."]
    substitution, sub_operations = edit_distance_recurse(s1_arr[1: ], s2_arr[1: ], sub_operations)
    
    # calculate minimum cost
    min_cost = min(insertion + ins_cost, deletion + del_cost, substitution + sub_cost)
    
    if min_cost == (substitution + sub_cost):
        return min_cost, sub_operations
    elif min_cost == deletion + del_cost:
        return min_cost, del_operations
    else:
        return min_cost, ins_operations

def error_counter(operations):
    i = 0
    d = 0
    s = 0
    for operation in operations:
        i = i + 1 if operation[0] == 'I' else i
        d = d + 1 if operation[0] == 'D' else d
        s = s + 1 if operation[0] == 'S' else s
    return i, d, s

def word_error_rate(text, error):
    return error/len(text.split())

s1 = input('Enter Reference Sentence: ')
s2 = input('Enter Hypothesis Sentence: ')
s1_arr = s1.split()
s2_arr = s2.split()
score, operations = edit_distance_recurse(s1_arr, s2_arr)
print(f"Levenshtein Distance between \n`{s1}` \nand \n`{s2}` \nis: {score}")

count_ins, count_del, count_sub = error_counter(operations)
print(f"\nsubstitution: {count_sub} \ninsertion: {count_ins} \ndeletion: {count_del}")

wer = word_error_rate(s1, score)
print(f"\nWord Error Rate(WER): {wer}")

print("\nOperations performed are:\n")
for operation in operations:
    print(operation)

