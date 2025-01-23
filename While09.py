def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    n = 0
    while n < len(s):
        if s[n].isdigit():
            count += int(s[n])
        n += 1
    return count