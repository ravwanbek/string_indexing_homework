def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s=str(s)
    answer=int(0)
    
    if s[0].isdigit():
        answer +=1

    if s[1].isdigit():
        answer +=1

    if s[2].isdigit():
        answer +=1

    if s[3].isdigit():
        answer +=1
    if s[4].isdigit():
        answer +=1
    
    return answer
print(main('s594d'))