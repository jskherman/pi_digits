def search_pi(sequence: str, pi_file: str = "pi-million.txt"):
    """
    This function takes in two arguments, a `sequence` of digits to be
    searched in pi and a `pi_file` containing pi digits with default value
    of "pi-million.txt"

    Parameters
    ----------
    sequence : str
        Sequence of digits of arbitrary length

    pi_file : str
        A string that is the filename of the file containing the digits of pi

    Returns
    -------
    str
        The position of the sequence in the file if found, else returns
        "Sequence not found in the decimal digits of pi"

    Examples
    --------
    >>> search_pi("123")
    1924
    >>> search_pi("123456789", "pi-billion.txt")
    523551502
    """

    # Import the mmap module
    import mmap

    # This line opens the file with the name of `pi_file` passed in the
    # argument, in read mode and assigns the file object to f
    with open(pi_file, "r") as f:

        # Memory map the file object f, with f.fileno()
        # as file descriptor and access mode as read-only
        pi_digits = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # Find the position of the sequence passed in the argument in the
        # memory mapped pi_digits. Since the `mmap()` method returns a
        # memory-mapped object and `find()` method expect bytes, we need to
        # encode the input sequence.
        position = pi_digits.find(sequence.encode())

    # This line checks if the position returned by find is -1 or not
    if position == -1:

        # if position is -1, returns "Sequence not found in the decimal digits of pi"
        return "Sequence not found in the decimal digits of pi"
    else:
        # if position is not -1, returns position - 1
        return position - 1
