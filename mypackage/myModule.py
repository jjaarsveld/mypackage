def top_n(items, n):
    """ Return the top n items in an array, in descending order.

    Args:
        items (array): list of array-like objects
        n (int): number of items to return

    Return:
        array: top n items, in descending order

    eg:
    >>> top_n([8,3,2,7,4], 3)
    [8, 7, 4]
    """

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i): #if this item is bigger than the next items
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    #get the last two items
    top_n = items[-n:]

    return  top_n[::-1]

