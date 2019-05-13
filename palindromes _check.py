from pythonds import Stack


def check_palindromes(litral: str) -> None:
    stack = Stack()
    for s in litral:
        if s != ' ':
            stack.push(s)
    litral = ''
    reverse = ''
    while not stack.isEmpty():
        last = stack.pop()
        litral = last + litral
        reverse += last
    return reverse == litral


print(check_palindromes('I PREFER PI'))
