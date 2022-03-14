def digitize(n):
    mass = []
    for i in str(n)[::-1]:
        mass.append(int(i))
    return mass