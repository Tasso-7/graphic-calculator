from turtle import *
import elab

def cartesian_generation(pos_X,pos_Y,sizeX,sizeY):
    penup()
    goto(pos_X,pos_Y)
    pendown()
    goto(pos_X,pos_Y + sizeY)
    goto(pos_X,pos_Y - sizeY)
    penup()
    goto(pos_X-sizeX,pos_Y)
    pendown()
    goto(pos_X+sizeX,pos_Y)
    goto(pos_X,pos_Y)

def showfunction(pos_X,pos_Y,sizeX,sizeY,pixel_value):
    pass