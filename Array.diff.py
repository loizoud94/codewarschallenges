def array_diff(a, b):

    # work with a new list to keep 'a' in tact if needed again.
    c = a.copy()

    # force 'b' to feature unique items only
    d =[]
    for i in b:
        if i not in d:
            d.append(i)

    # iterate across each item in 'a' and 'd' to return only the items in 'a' that don't appear in 'd'.
    for i in d:
        for j in a:
            if i == j:
                c.remove(i)
    return c
