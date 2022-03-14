def abbrev_name(name):
    first = name.split(' ')[0][0]
    second = name.split(' ')[1][0]
    result = first + '.' + second
    return result.upper()