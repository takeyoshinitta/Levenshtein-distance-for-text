import numpy as np

# Below are the costs of different operations.
ins_cost = 1
del_cost = 1
sub_cost = 1

# Below function will take the two sequence and will return the distance between them.
def edit_distance_recurse(s1_arr, s2_arr, operations=[]):
    """Returns the Edit Distance between the provided two sequences."""
    
    if len(s1_arr) == 0:
        operations = operations + ([f"Delete `{s1_arr}` from sequence1."] if len(s1_arr) else [])
        return len(s1_arr), operations
    
    if len(s2_arr) == 0:
        operations = operations + ([f"Insert `{s2_arr}` into sequence1."] if len(s2_arr) else [])
        return len(s2), operations
    
    if s1_arr[0] == s2_arr[0]:
        operations = operations + [f"Make no change for character `{s1_arr[0]}`."]
        return edit_distance_recurse(s1_arr[1: ], s2_arr[1: ], operations)
    
    # calculate cost if insertion was made
    ins_operations = operations + [f"Insert `{s2_arr[0]}` in sequence1."]
    insertion, ins_operations = edit_distance_recurse(s1_arr, s2_arr[1: ], ins_operations)
    
    # calculate cost if deletion was done
    del_operations = operations + [f"Delete `{s1_arr[0]}` from sequence1."]
    deletion, del_operations = edit_distance_recurse(s1_arr[1: ], s2_arr, del_operations)
    
    # calculate cost if substitution was done
    sub_operations = operations + [f"Replace `{s1_arr[0]}` in sequence1 with `{s2_arr[0]}`."]
    substitution, sub_operations = edit_distance_recurse(s1_arr[1: ], s2_arr[1: ], sub_operations)
    
    # calculate minimum cost
    min_cost = min(insertion + ins_cost, deletion + del_cost, substitution + sub_cost)
    
    if min_cost == (substitution + sub_cost):
        return min_cost, sub_operations
    elif min_cost == deletion + del_cost:
        return min_cost, del_operations
    else:
        return min_cost, ins_operations


def min_cost_path(cost, operations):
    
    # operation at the last cell
    path = [operations[cost.shape[0]-1][cost.shape[1]-1]]
    
    # cost at the last cell
    min_cost = cost[cost.shape[0]-1][cost.shape[1]-1]
    
    row = cost.shape[0]-1
    col = cost.shape[1]-1
    
    while row >0 and col > 0:
            
        if cost[row-1][col-1] <= cost[row-1][col] and cost[row-1][col-1] <= cost[row][col-1]:
            path.append(operations[row-1][col-1])
            row -= 1
            col -= 1
        elif cost[row-1][col] <= cost[row-1][col-1] and cost[row-1][col] <= cost[row][col-1]:
            path.append(operations[row-1][col])
            row -= 1
        else:
            path.append(operations[row][col-1])
            col -= 1
                    
    return "".join(path[::-1][1:])

def edit_distance_dp(seq1, seq2):
    
    # create an empty 2D matrix to store cost
    cost = np.zeros((len(seq1)+1, len(seq2)+1))
    
    # fill the first row
    cost[0] = [i for i in range(len(seq2)+1)]
    
    # fill the first column
    cost[:, 0] = [i for i in range(len(seq1)+1)]
    
    # to store the operations made
    operations = np.asarray([['-' for j in range(len(seq2)+1)] \
                                 for i in range(len(seq1)+1)])
    
    # fill the first row by insertion 
    operations[0] = ['I' for i in range(len(seq2)+1)]
    
    # fill the first column by insertion operation (D)
    operations[:, 0] = ['D' for i in range(len(seq1)+1)]
    
    operations[0, 0] = '-'
    
    # now, iterate over earch row and column
    for row in range(1, len(seq1)+1):
        
        for col in range(1, len(seq2)+1):
            
            # if both the characters are same then the cost will be same as 
            # the cost of the previous sub-sequence
            if seq1[row-1] == seq2[col-1]:
                cost[row][col] = cost[row-1][col-1]
            else:
                
                insertion_cost = cost[row][col-1] + ins_cost
                deletion_cost = cost[row-1][col] + del_cost
                substitution_cost = cost[row-1][col-1] + sub_cost
                
                # calculate the minimum cost
                cost[row][col] = min(insertion_cost, deletion_cost, substitution_cost)
                
                # get the operation
                if cost[row][col] == substitution_cost:
                    operations[row][col] = 'S'
                    
                elif cost[row][col] == ins_cost:
                    operations[row][col] = 'I'
                else:
                    operations[row][col] = 'D'
                
    return cost[len(seq1), len(seq2)], min_cost_path(cost, operations)

s1 = input('Enter Reference Sentence: ')
s2 = input('Enter Hypothesis Sentence: ')
s1_arr = s1.split()
s2_arr = s2.split()
score, operations = edit_distance_recurse(s1_arr, s2_arr)
print(f"Levenshtein Distance between `{s1}` & `{s2}` is: {score}")
print("\nOperations performed are:\n")
for operation in operations:
    print(operation)

print("\n")

score, operations = edit_distance_dp(s1_arr, s2_arr)
print(f"Edit Distance between `{s1}` & `{s2}` is: {score}")
print("\nOperations performed are:\n")
for operation in operations:
    if operation == '-':
        print('No Change.')
    elif operation == 'I':
        print('Insertion')
    elif operation == 'D':
        print('Deletion')
    else:
        print('Substitution')