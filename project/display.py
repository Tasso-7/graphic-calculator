from turtle import *
import elab,main

def cartesian_generation(pos_X,pos_Y,sizeX,sizeY,pixel_value,offset):
    #x and y axis
    color("gray")
    pensize(4)
    clear()

    penup()
    goto(pos_X,pos_Y + sizeY)
    pendown()
    goto(pos_X,pos_Y - sizeY)
    penup()

    goto(pos_X-sizeX,pos_Y)
    pendown()
    goto(pos_X+sizeX,pos_Y)
    pensize(2)
    color("light gray")

    pixel_1 = 1/pixel_value

    #other elements
    
    for j,size in enumerate([sizeY,sizeX]):
        actual = (-size)
        while not actual%pixel_1 == 0:
            actual += 1

        while actual < size:
            actual += pixel_1
            penup()
            if j == 0:
                goto((pos_X - offset),actual + pos_Y)
                pendown()
                goto((pos_X + offset),actual + pos_Y)

            else:
                goto(actual + pos_X, (pos_Y - offset))
                pendown()
                goto(actual + pos_X, (pos_Y + offset))

    pensize(1)
    color("black")

def display_function(pos_X,sizeX,data,pos_Y):
    penup()
    goto(pos_X-sizeX,(pos_Y))
    pendown()
    x = pos_X - sizeX
    for i in data.items():
        try:
            goto(x,i[1])
            pendown()
            x += 1
        except:
            penup()
            goto(x,0)
            x += 1  

def get_function_data(pos_X,pos_Y,sizeX,sizeY,pixel_value,operation):
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

    return newdata

def derivated(pos_X,pos_Y,sizeX,sizeY,pixel_value,operation):
    operation = elab.fixed_operation(operation)
    values = {}
    data = {}
    lastevalue = pixel_value * (0-sizeX)
    for i in range(pos_X-sizeX,pos_X+sizeX+1):
        values[i] = lastevalue
        lastevalue += pixel_value

    for j,i in values.items():
        if(not (i == 0 or i == 1 or i == -1)):
            data[j] = (((elab.elab(operation,i+pixel_value) / pixel_value) + pos_Y)-((elab.elab(operation,i) / pixel_value) + pos_Y))/pixel_value
        else:
            data[j] = 0
    newdata = {}
    for j,i in data.items():
        newdata[j] = elab.clamp(i,-sizeY + pos_Y,sizeY + pos_Y)

    return newdata

def showfunction(pos_X,pos_Y,sizeX,sizeY,pixel_value,operation):
    data = get_function_data(pos_X,pos_Y,sizeX,sizeY,pixel_value,operation)
    pensize(3)
    color("red")
    display_function(pos_X,sizeX,data,pos_Y)
    color("green")
    display_function(pos_X,sizeX,derivated(pos_X,pos_Y,sizeX,sizeY,pixel_value,operation),pos_Y)
    return data

if __name__ == "__main__":    main.Main()