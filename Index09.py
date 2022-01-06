def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    
    s=str(s)

    if s.isdigit():
        answer=int(s)
    else:
        answer=-1

    return answer
    
print(main('7'))