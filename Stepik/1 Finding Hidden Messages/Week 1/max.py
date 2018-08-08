def max(list):
    m = list[0] 
    for item in list:
        if item > m: 
            m = item
    return m 