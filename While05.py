def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    n = 0
    while n < len(s):
        if s[n].islower():
            count += 1
        n += 1
    return count