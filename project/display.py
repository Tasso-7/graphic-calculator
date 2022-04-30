from turtle import *
import elab

def cartesian_generation(pos_X,pos_Y,sizeX,sizeY):
    clear()
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

def display_function(pos_X,pos_Y,sizeX,data):
    penup()
    goto(pos_X-sizeX,pos_Y)
    pendown()
    x = pos_X - sizeX
    for i in data.items():
        goto(x,i[1])
        x += 1  

def showfunction(pos_X,pos_Y,sizeX,sizeY,pixel_value,operation):
    operation = elab.fixed_operation(operation)
    values = {}
    data = {}
    lastevalue = pixel_value * (0-sizeX)
    for i in range(pos_X-sizeX,pos_X+sizeX+1):
        values[i] = lastevalue
        lastevalue += pixel_value
    for j,i in values.items():
        if(not (i == 0 or i == 1 or i == -1)):
            data[j] = (elab.elab(operation,i) / pixel_value) + pos_Y
        else:
            data[j] = 0
    newdata = {}
    for j,i in data.items():
        newdata[j] = elab.clamp(i,-sizeY + pos_Y,sizeY + pos_Y)
    data = newdata
    display_function(pos_X,pos_Y,sizeX,data)
    return data