def main(s):
    """
    The s string variable is given. Return three characters from the beginning.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s=str(s)
    answer=s[0:3]
    return answer
print(main('chevrolet'))