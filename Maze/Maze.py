import random
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        # 迷宫左下角坐标（-10.5 ，-5.5）右上角坐标 (10.5, 5.5)
        self.wn.setworldcoordinates(-(columnsInMaze - 1) / 2 - .5, -(rowsInMaze - 1) / 2 - .5,
                                    (columnsInMaze - 1) / 2 + .5, (rowsInMaze - 1) / 2 + .5)
        # print(-(columnsInMaze - 1) / 2 - .5, -(rowsInMaze - 1) / 2 - .5, (columnsInMaze - 1) / 2 + .5,
        #       (rowsInMaze - 1) / 2 + .5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)  # 不显示画图过程
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    # 画一个长度为一个单位的正方形（由于横竖坐标单位长度不一致，看起来并不是正方形）
                    # 二维列表的索引向坐标转换
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')  #
        self.t.color('black')
        self.t.fillcolor('green')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    # 指向目标索引，转化坐标，让乌龟指向目标坐标并跳跃过去
    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))  # 索引转换坐标
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(10, color)

    def updatePosition(self, row, col, val=None):  # 参数是索引
        if val:
            self.mazelist[row][col] = val  # 指定该列表元素被赋值的对象
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or
                row == self.rowsInMaze - 1 or
                col == 0 or
                col == self.columnsInMaze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]


def searchFrom(maze: Maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # 增加随机选择查找顺序
    # 四个参数组
    choices = [(maze, startRow + 1, startColumn), (maze, startRow - 1, startColumn), (maze, startRow, startColumn + 1),
               (maze, startRow, startColumn - 1)]
    random.Random().shuffle(choices)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(*choices[0]) or \
            searchFrom(*choices[1]) or \
            searchFrom(*choices[2]) or \
            searchFrom(*choices[3])

    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
