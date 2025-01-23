def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    n = 0
    while n < len(s):
        if int(s[n]) % 2 == 1:
            count += 1
        n += 1
    return count