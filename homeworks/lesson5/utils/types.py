def isfloat(s):
    """
    Checks if passed string can be converted to float

    :param s: str
    :return: bool
    """
    try:
        float(s)
        return True
    except ValueError:
        return False
