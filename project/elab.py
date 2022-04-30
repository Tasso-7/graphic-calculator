def elab(operation,x_value):
    return eval(operation.replace("x",str(x_value)))

def clamp(num,min,max):
    if num <= min:
        return min
    elif num >= max:
        return max
    else:
        return num