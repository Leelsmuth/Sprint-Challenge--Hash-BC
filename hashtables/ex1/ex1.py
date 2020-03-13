#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    
    for i in range(length):
        # find match based on current index locations value
        difference = limit - weights[i]
        # get current value from hashtable
        match = hash_table_retrieve(ht, difference)
        if match is not None:
            # if match found return with current index first
            return [i, match]
        # else no match build the hashtable 
        hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
