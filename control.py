def choose_action(s1, s2, s3, s4, t):

    if s1 > t and s2 > t and s3 > t and s4 > t:
        return "Continue"
    elif s1 <= t and s2 <= t and s3 <= t and s4 <= t:
        return "Trapped"
    elif s2 <= t and s3 <= t and s4 <= t:
        return "N"
    elif s1 <= t and s3 <= t and s4 <= t:
        return "E"
    elif s1 <= t and s2 <= t and s3 <= t:
        return "W"
    elif s1 <= t and s2 <= t and s4 <= t:
        return "S"
    elif s3 <= t and s4 <= t:
        return "NE"
    elif s2 <= t and s4 <= t:
        return "N or S"
    elif s2 <= t and s3 <= t:
        return "NW"
    elif s1 <= t and s4 <= t:
        return "SE"
    elif s1 <= t and s3 <= t:
        return "E or W"
    elif s1 <= t and s2 <= t:
        return "SW"
    elif s4 <= t:
        return "E"
    elif s3 <= t:
        return "N"
    elif s2 <= t:
        return "W"
    elif s1 <= t:
        return "S"


















