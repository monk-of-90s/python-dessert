from pythonds.basic.stack import Stack


def HTML_tags_check(html: str):
    stack = Stack()
    # 记录整个tag
    tempstr = ''
    for s in html:
        # 只暂存tag
        if tempstr.find('<') >= 0 or s == '<':
            tempstr += s
        # 存储完整头tag进stack
        if s == '>':
            if tempstr.find('/') < 0:  # 头tag检测完毕
                stack.push(tempstr)
            else:  # 尾tag暂存完毕
                last_str_list = list(stack.pop())
                last_str_list.insert(1, '/')
                tag_to_match = ''.join(last_str_list)
                if tag_to_match != tempstr:
                    return False
            tempstr = ''

    if not stack.isEmpty():
        return False
    return True


print(HTML_tags_check('''
<html>
   <head>
      <title>
         Example
      </title>
   </head>
<title>
tryrtr
</title>
   <body>
      <h1>Hello, world</h1>
   </body>
</html>'''))
