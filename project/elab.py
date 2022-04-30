def elab(operation,num):
    return eval(operation.replace("x",str(num)))

def fixed_operation(operation):
    operations = ["+","-","*","/","%"]
    x = False
    op = False
    newoperation = ""
    for i in operation:
        op = False
        if i == x:
            x = True
            if not op:
                newoperation += "*x"
        else:
            if not x:
                newoperation += i
            else:
                now_op = False
                for j in operations:
                    if j == i:
                        now_op = True
                if now_op:
                    newoperation += i
                else:
                    newoperation += "*" + i
                
        for j in operations:
            if j == i:
                op = True
    return newoperation
