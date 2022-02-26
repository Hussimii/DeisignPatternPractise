def add(arg):
    """
    >>> add('12')
    146
    """
    return float(arg)+4


if __name__ == '__main__':
    import doctest
    doctest.testmod()
