def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    count = 0
    n = 0
    while n < len(s):
        if s[n].isalpha() and s[n].lower() not in "aeiou":
            count += 1
        n += 1
    return count