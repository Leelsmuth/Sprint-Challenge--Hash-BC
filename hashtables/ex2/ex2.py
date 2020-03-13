#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)
    """
    YOUR CODE HERE
    """
    last_key = "NONE"
    
    # Insert locations on hash table
    for location in range(0, len(tickets)):
        hash_table_insert(hashtable, tickets[location].source, tickets[location].destination)
    
    # loop through and set the next destinatin on the list
    for location in range(0, len(route)):
        found = hash_table_retrieve(hashtable, last_key)
        if found is not None and found is not "NONE":
            route[location] = found
            last_key = found
    return route