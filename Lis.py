"""
Project 7 - Longest Increasing Subsequence
Uses 3 methods
First, determines whether a subsequence exists
Then determines if a subsequence is increasing by comparing each item to its next successor
Finally, finds the longest increasing subsequence using the Patience Algorithm.
"""

def verify_subseq(seq, subseq):
    """
    Determines whether or not a sequence contains a certain subsequence.
    Does not have to be in increasing order.
    :param seq: sequence
    :param subseq: subsequence
    :return: True if sequence contains subsequence, False otherwise.
    """
    it = iter(seq)  # create iterator of seq

    for ch in subseq:       # go through subseq
        if ch not in it:    # if ch is not in what's left of iterator
            return False    # seq does not exist

    return True     # seq exists

def verify_increasing(seq):
    """
    Verifies if a sequence is in increasing order.
    Zips two lists: one without first item and one without last item
    So you can compare each item in the list with its next item
    :return: True if increasing order, False otherwise.
    """
    if not seq:         # if seq is empty
        return True

    seq = [ch for ch in seq]    # convert to a list
    comp_seq = seq[1:]          # make separate list without first item
    seq.pop()                   # remove last item from original list

    # True if every item is less than than its successor
    result = all(j < k for j, k in zip(seq, comp_seq))

    return result

def find_lis(seq):
    """
    Finds longest increasing subsequence within a given sequence
    Patience Algorithm is used to create stacks to find LIS
    Implemented using a list of lists ("stacks")
    Pointer to previous index is kept track of for each item in seq
    Previous index is followed from last item in largest stack to find LIS
    :return: List including the LIS
    """
    lis_stacks = []          # will be list of lists of each ch and its corresponding index
    prev_indices = [None for _ in seq]     # each item in seq has an previous item in LIS
    lis = []                               # empty lis list to return

    if not seq:     # if sequence is empty
        return lis

    if len(seq) == 1:   # if sequence only contains one item
        return [i for i in seq]

    for i, ch in enumerate(seq):
        if not lis_stacks:                      # if there are no stacks yet
            lis_stacks.append([[ch, i]])        # add first stack

        elif ch <= lis_stacks[0][-1][0]:         # check if new ch should be added to first stack
            lis_stacks[0].append([ch, i])

        elif ch > lis_stacks[-1][-1][0]:                # check if ch is new largest value
            lis_stacks.append([[ch, i]])                # add new stack to end
            prev_indices[i] = lis_stacks[-2][-1][1]     # link top item from prev stack as prev

        else:                                           # ch must be added in some middle stack
            for j, sublist in enumerate(lis_stacks):
                if ch <= sublist[-1][0]:                # check last item in each stack
                    sublist.append([ch, i])             # add if ch is less than or equal
                    prev_indices[i] = lis_stacks[j-1][-1][1]    # prev item is last item in prev stack
                    break

    last_item_index = lis_stacks[-1][-1][1]     # get last item from last stack
    lis.append(seq[last_item_index])            # add it to lis

    current = prev_indices[last_item_index]     # set current to prev index of last item

    while current is not None:              # loop through til we get to the last item
        lis.append(seq[current])            # add each previously-pointed-to item to lis list
        current = prev_indices[current]     # set current to its previous index

    lis.reverse()       # reverse list since we added items to lis in reverse order
    return lis
