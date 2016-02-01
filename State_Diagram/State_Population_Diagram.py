import turtle
from states_1 import make
t = turtle.setup(width=900,height=700)
turtle.up()
turtle.setpos(250,300)

s=['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
   'Connecticut','Delaware','District of Columbia','Florida','Georgia',
   'Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
   'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
   'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
   'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
   'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
   'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia',
   'Wisconsin','Wyoming']
y = 300
x=51
z = 0
#Begin to write the names of the states in the correct spots.
turtle.pencolor('red')
while x>0:
    y= y - 12
    turtle.write(s[z] ,font = ('Times New Roman',10,'bold'))
    x= x-1
    turtle.setpos(250,y)
    z = z + 1
p = 0
x=51
Y = 322
turtle.pencolor('green')
#Begin to draw the squares for each states population using the dictionary.
while x>0:
    Y = Y - 12
    D = make()
    State = s[p]
    D = D[State]
    D = D.pop()
    D = float(D)
    POP = D / 1000000
    x = x - 1
    p = p + 1          
    X=240
    STATE = 51
    if POP>1:
        X = 240
        while STATE>0:
            STATE = STATE - 1
            S1 = 4
            while POP>=1:
                turtle.up()
                turtle.setpos(X,Y)
                turtle.down()
                turtle.begin_fill()
                turtle.color('green')
                turtle.right(180)
                turtle.forward(10)
                turtle.left(90)
                turtle.forward(8)
                turtle.left(90)
                turtle.forward(10)
                turtle.left(90)
                turtle.forward(8)
                turtle.right(90)
                turtle.end_fill()
                POP = POP - 1
                X = X - 15
                turtle.fillcolor()
    if 0<POP<1:
         F = POP * 10
         turtle.up()
         turtle.setpos(X,Y)
         turtle.down()
         turtle.begin_fill()
         turtle.color('green')
         turtle.right(180)
         turtle.forward(F)
         turtle.left(90)
         turtle.forward(8)
         turtle.left(90)
         turtle.forward(F)
         turtle.left(90)
         turtle.forward(8)
         turtle.right(90)
         turtle.end_fill()
         POP = POP - 1
         turtle.fillcolor('green')
turtle.up()
