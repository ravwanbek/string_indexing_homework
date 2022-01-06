def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s=str(s)
    answer=s.rfind('*')
    if answer ==-1:
        answer=False
    
    
    return answer
print(main('s556d'))
        