import introcs

def second_in_list(s):
    """
    Returns: the second item in comma-separated list

    The final result should not have any whitespace around the edge

    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list(' do, re, me, fa ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'

    Parameter s: The list of items

    Precondition: s is a string of at least three items separated by commas
    """
    assert type(s) == str, "The value {} is not a string.".format(repr(s))
    assert introcs.count_str(s, ',') >= 2

    first = introcs.find_str(s, ',')
    second = introcs.find_str(s, ',', first + 1)
    slice = s[first + 1: second]
    result = introcs.strip(slice)
    return result
