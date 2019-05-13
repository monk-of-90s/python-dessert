from pythonds.basic import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            found = False
            while topToken != '(' and not opStack.isEmpty():
                found = True
                postfixList.append(topToken)
                topToken = opStack.pop()
            if not found:
                raise Exception('Unbalanced parentheses,too much ")"')
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    unbalanced_found = False
    while not opStack.isEmpty():
        last = opStack.pop()
        if last == '(':
            unbalanced_found = True
            raise Exception('Unbalanced parentheses,too much "("')
        postfixList.append(last)
    return " ".join(postfixList)


print(infixToPostfix("( ( A * B + ( C * D ) )"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
