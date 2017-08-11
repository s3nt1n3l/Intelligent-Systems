import turtle, random

#Create window
window = turtle.Screen()
window.title("Maze")
window.setup(315,315)
window.bgcolor("orange")

#Defines maze blocks
class blocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.speed(0)
        self.penup()

#Defines Movement blocks
class Mblocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.speed(1)

#Defines end block
class Eblocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.speed(0)
        self.penup()

#Defines wall block hit by search
class Wblocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.speed(0)
        self.penup()
        
        
#Defines grid of blocks
grid = [
['0','0','0','0','0','0','0','0','0','0','0'],
['1','1','0','0','1','0','1','1','1','1','0'],
['0','1','1','1','1','0','1','0','0','0','0'],
['0','1','0','0','1','1','1','1','1','1','0'],
['0','1','0','0','1','0','0','0','0','1','0'],
['0','1','1','1','1','1','1','1','1','1','0'],
['0','0','0','1','0','0','0','0','1','0','0'],
['0','1','0','1','0','1','1','1','1','1','0'],
['0','1','0','1','0','0','0','0','0','0','0'],
['0','1','0','1','1','1','1','1','1','1','0'],
['0','0','0','0','0','0','0','0','0','E','0']
]

#creates grid of blocks
def createGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            #gets screen size
            sx = -126 + (x * 24)
            sy = 126 - (y * 24)
            #checks if current block is a wall
            if char == '0':
                pen.goto(sx,sy)
                pen.stamp()
            elif char == 'E':
                Yellowpen.goto(sx,sy)
                Yellowpen.stamp()


def moveTo(x, y):
    sx = -126 + (x * 24)
    sy = 126 - (y * 24)
    char = grid[y][x]
    if char == 'E':
        print('End of maze at %d,%d' % (x, y))
        #Found end of maze
        return True
    
    elif char == '0':
        print('Hit a wall at %d,%d' % (x, y))
        Redpen.goto(sx,sy)
        Redpen.stamp
        #hits a wall and backtracks
        return False
    
    elif char == 'V':
        print('Already visited %d,%d' %(x, y))
        Redpen.goto(sx,sy)
        Redpen.stamp
        #back tracks to find new path
        return False
    
    print('Going to %d,%d' % (x, y))
    Greenpen.goto(sx,sy)
    Greenpen.stamp

    #mark as visited
    grid[y][x] = 'V'
    print('Mark as visited %d, %d' % (x, y))
    
    #go to neighbors
        #Right
    if (x < len(grid)-1 and moveTo(x+1, y)
        #Under
        or (y < len(grid)-1 and moveTo(x, y+1))
        #Left
        or (x > 0 and moveTo(x-1, y))
        #Above
        or ((y > 0 and moveTo(x, y-1)))):
        return True

    return False

#Makes class instance
pen = blocks()

#Makes class instance
Greenpen = Mblocks()

#Makes class instance
Yellowpen = Eblocks()

#Makes class instance
Redpen = Wblocks()

#setup grid
createGrid(grid)

#Starting point
moveTo(0,1)
