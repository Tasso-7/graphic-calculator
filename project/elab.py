def elab(operation,num):
    return eval(operation.replace("x",str(num)))

def clamp(num,min,max):
    if num <= min:
        return min
    elif num >= max:
        return max
    else:
        return num

def fixed_operation(operation):
    operations = ["+","-","*","/","%"]
    x = False
    op = False
    precedent_op = False
    newoperation = ""
    for i in operation:
        precedent_op = op
        op = False
        for j in operations:
            if j == i:
                op = True
        if i == "x":
            x = True
            if not (op or precedent_op):
                newoperation += "*x"
            else:
                newoperation += "x"
        else:
            if not x:
                newoperation += i
            else:
                if op or precedent_op:
                    newoperation += i
                else:
                    newoperation += "*" + i
                x = False
    return newoperation