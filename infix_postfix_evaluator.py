from pythonds.basic import Stack


def direct_infix_evaluator(infixexpr: str) -> int or float:
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixEvaluation = Stack()
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixEvaluation.push(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            found = False
            while topToken != '(' and not opStack.isEmpty():
                found = True
                operator = topToken
                operand2 = postfixEvaluation.pop()
                operand1 = postfixEvaluation.pop()
                postfixEvaluation.push(doMath(operator, operand1, operand2))
                topToken = opStack.pop()
            if not found:
                raise Exception('Unbalanced parentheses,too much ")"')
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                operator = opStack.pop()
                operand2 = postfixEvaluation.pop()
                operand1 = postfixEvaluation.pop()
                postfixEvaluation.push(doMath(operator, operand1, operand2))
            opStack.push(token)
    unbalanced_found = False
    while not opStack.isEmpty():
        last = opStack.pop()
        if last == '(':
            unbalanced_found = True
            raise Exception('Unbalanced parentheses,too much "("')
        operator = last
        operand2 = postfixEvaluation.pop()
        operand1 = postfixEvaluation.pop()
        postfixEvaluation.push(doMath(operator, operand1, operand2))
    return postfixEvaluation.pop()


def doMath(op, op1, op2):
    op1 = float(op1)
    op2 = float(op2)
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(direct_infix_evaluator('( 1 + 2 ) * 3 - 3 / 4'))
