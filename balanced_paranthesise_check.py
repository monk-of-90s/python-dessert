from pythonds.basic import Stack


def parChecker(pstr: str):
    s = Stack()
    try:
        index = 0
        while index < len(pstr):
            if pstr[index] in '([{':
                s.push(pstr[index])
            elif ')]}'.index(pstr[index]) != '([{'.index(s.pop()):  # ')]}'.index()  :
                return False
            index += 1
    except:
        return False
    if s.isEmpty():
        return True
    else:
        return False


print(parChecker('{{([][])}()})'))
print(parChecker('[{()}]'))
