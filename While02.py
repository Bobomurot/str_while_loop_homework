def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    n = len(s)
    while n < len(s):
        if s[n].isalpha():
            count += 1
        n += 1
    return count