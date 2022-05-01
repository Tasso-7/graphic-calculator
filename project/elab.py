import main,math

def abs(num):
    if num >= 0:
        return num
    else:
        return num * -1

def sin(angle):
    return math.sin(angle)

def cos(angle):
    return math.cos(angle)

def tan(angle):
    return math.tan(angle)

def log(base,num):
    return math.log(num,base)

def sqrt(num):
    return math.sqrt(num)

def factorial(num):
    return math.factorial(num)

def MCD(n1,n2):
    if n2 == 0:
        return n1
    else:
        return MCD(n2,n1%n2)

def mcm(n1,n2):
    return (n1 * n2) / MCD(n1,n2)

def clamp(num,min,max):
    if num <= min:
        return min
    elif num >= max:
        return max
    else:
        return num

def elab(operation,num):
    x = eval(operation.replace("x",str(num)).replace("^","**"))
    return x

operations = ["+","-","*","/","%","^","=",",","(",")"]

def fixed_operation(operation):
    global operations
    x = False
    op = True
    precedent_op = True
    close_brackets = False
    newoperation = ""
    for i in operation:
        precedent_op = op
        op = False
        for j in operations:
            if j == i:
                op = True
        if i == "x":
            x = True
            if not (op or precedent_op or close_brackets):
                newoperation += "*x"
            else:
                newoperation += "x"
            close_brackets = False
        elif x == ")":
                close_brackets = True
        else:
            if not x:
                newoperation += i
            else:
                if op or precedent_op:
                    newoperation += i
                else:
                    newoperation += "*" + i
                x = False
            close_brackets = False
    return newoperation

if __name__ == "__main__":
    main.Main()