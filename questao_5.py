def reverte_string(string):
    res = ''
    i = len(string)
    while i > 0:
        res = res + string[i - 1]
        i = i - 1
    print(res)
