from turtle import *
def stairs(size,number):
    for i in range(0, number):
        forward(size)
        left(90)
        forward(size)
        right(90)
        size -= 10
    forward(size)

def square(size):
    for i in range(0, 4):
        forward(size)
        left(90)

def squares(size_New ,number):
    for i in range(0, number):
        size =(i+1)*size_New
        square(size)

reset()
# stairs(100,5)
# square(40)
squares(10,10)
done()