from turtle import*
import winsound

t = Turtle()
side = 10
t.width(1)
numSquares = 16
t.speed (0)

w = 'white'
b = 'black'
r = 'red'
bl = 'blue'
p = 'pink'

number = []
colors = []

winsound.PlaySound("mario_08.wav",winsound.SND_ASYNC)

def drawSquare(color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.rt(90)
    t.end_fill()
    t.forward(side)

def nextRow():
    t.pu()
    t.backward(numSquares*side)
    t.lt(90)
    t.forward(side)
    t.rt(90)
    t.pd()

def drawRow(color, numbers):
    for j in range(len(colors)):
        for k in range(numbers[j]):
            drawSquare(colors[j])
    nextRow()

#Mario
#row1
colors =[w, b, w]
numbers =[1, 2, 13]
drawRow(colors, numbers)

#row2
colors = [b, r, b, w, b, w]
numbers = [1, 2, 2, 7, 3, 1]
drawRow(colors, numbers)

#row3
colors = [b, r, b, bl, b, w, b, r, b]
numbers = [1,2,1,1,3,3,1,2,2]
drawRow(colors, numbers)

#row4
colors = [b, r, b, bl, b, r, b]
numbers = [1,2,1,4,4,3,1]
drawRow(colors, numbers)

#row5
colors = [b,r,b,bl,b,r,b]
numbers = [2,1,1,7,1,3,1]
drawRow(colors, numbers)

#row6
colors = [w,b,r,b,bl,b,r,b]
numbers = [1,1,2,3,4,1,3,1]
drawRow(colors, numbers)

#row7
colors = [w,b,w,b,bl,w,bl,b,r,b]
numbers = [2,2,3,1,1,2,1,1,2,1]
drawRow(colors, numbers)

#row8 double check from here
colors = [w,b,w,b,w,b,w,b,w]
numbers = [1,2,5,1,2,2,1,1,1]
drawRow(colors, numbers)

#row9
colors = [b,r,b,w,b,bl,b,r,b,w,]
numbers = [1,1,1,5,1,1,1,2,2,1]
drawRow(colors, numbers)

#row10
colors = [b,r,b,w,b,bl,b,r,b,w]
numbers = [1,2,1,3,1,1,1,3,1,2]
drawRow(colors, numbers)

#row11
colors = [b,r,b,bl,b,r,b,w]
numbers = [1,3,3,1,1,3,2,2]
drawRow(colors, numbers)

#row12
colors = [w,b,r,b,bl,b,r,b,w]
numbers = [1,1,4,1,1,1,2,2,3]
drawRow(colors, numbers)

#row13
colors = [w,b,r,b,r,b,w]
numbers = [2,1,3,6,1,1,2]
drawRow(colors, numbers)

#row14
colors = [w,b,p,b,r,b,w]
numbers = [3,3,5,1,2,1,1]
drawRow(colors, numbers)

#row15
colors = [w,b,p,b,r,b,w]
numbers = [2,2,4,5,1,1,1]
drawRow(colors, numbers)

#row16
colors = [w,b,p,b,p,b,w]
numbers = [1,1,4,4,2,3,1]
drawRow(colors, numbers)

#row17
colors = [b,p,b,p,b,p,b,r,b]
numbers = [1,3,1,2,1,5,1,1,1]
drawRow(colors, numbers)

#row18
colors = [b,p,b,p,b,r,b]
numbers = [1,2,3,7,1,1,1]
drawRow(colors, numbers)

#row19
colors = [w,b,p,b,p,w,b,p,b,w,b,r,b]
numbers = [1,1,1,2,2,1,1,1,1,1,1,2,1]
drawRow(colors, numbers)

#row20
colors = [w,b,p,w,b,p,b,w,b,r,b]
numbers = [1,4,2,1,1,1,1,1,1,2,1]
drawRow(colors, numbers)

#row21
colors = [w,b,r,b,p,w,p,w,b,w]
numbers = [2,1,1,2,1,2,1,2,3,1]
drawRow(colors, numbers)

#row22
colors = [w,b,r,b,w,b]
numbers = [2,1,3,8,1,1]
drawRow(colors, numbers)

#row23
colors = [w,b,r,b,w,b]
numbers = [3,1,3,6,2,1]
drawRow(colors, numbers)

#row24
colors = [w,b,r,w,r,b,w,b]
numbers = [4,1,3,2,1,1,3,1]
drawRow(colors, numbers)

#row25
colors = [w,b,r,b,w,b]
numbers = [5,2,3,2,3,1]
drawRow(colors, numbers)

#row26
colors = [w,b,w,b,w]
numbers =[7,4,1,3,1]
drawRow(colors, numbers)


write("Kelli Stasiak", align="right", font=("Arial", 40, 'bold'))






winsound.PlaySound("smb_gameover.wav",winsound.SND_ALIAS)




done()



