import turtle as bob

def drawRectangle():
    bob.color("red")
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)

def drawTriangle():
    bob.color("blue")
    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    bob.left(120)
    bob.forward(100)

def geo():
    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            bob.color(c)
            bob.forward(steps)
            bob.right(30)
    


drawRectangle()
bob.home()
drawTriangle()
bob.home()
geo()
