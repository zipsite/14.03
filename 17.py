def fake_bin(x):
    result = ''
    for i in range(len(x)):
        if int(x[i]) < 5:
            result += "0" 
        else:
            result += "1"
    return result