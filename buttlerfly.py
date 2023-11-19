import turtle
import random

def Dragon(iteration):
    seq = "FX"
    seq2 = ""
    
    for _ in range(iteration):
        for char in seq:
            if char == "X":
                seq2 += "X+YF+"
            elif char == "Y":
                seq2 += "-FX-Y"
            else:
                seq2 += char
        seq = seq2
        seq2 = ""

    return seq

def draw_dragon():
    dragon = Dragon(10)

    window = turtle.Screen()
    window.bgcolor("white")
    alex = turtle.Turtle()
    alex.speed(0)

    alex.color("black")
    alex.pensize(2)
    
    for move in dragon:
        if move == "F":
            alex.forward(10)
        elif move == "+":
            alex.right(90)
        elif move == "-":
            alex.left(90)

    turtle.done()

draw_dragon()

