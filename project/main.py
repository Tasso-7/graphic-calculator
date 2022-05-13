import display

            #True/False
all_offest = False

data_to_get = [
    ["position x: ", int,0 ],
    ["position y: ", int, 0],
    ["size x: ", int, 960],
    ["size y: ", int, 540],
    ["pixel value: ", float, 0.025],
    ["operation: ", str, "1/x"]
]

def ask_info(datatipe,question,predef):
    x = ""
    while True:
        error = True
        try:
            x = input(question + f"({predef})")
            x.replace("x","(x)")
            if x.strip() == "":
                error = False
                return predef
            if datatipe == int:
                x = int(x)
                error = False
            elif datatipe == float:
                x = float(x)
                error = False
            elif datatipe == str:
                error = False
            return x
        finally:
            if error:
                print("not valid")
        
def ask_data(all_offest):
    global data_to_get
    data = []
    for question,_type,normal in data_to_get:
        data.append(ask_info(_type,question,normal))
    for j,i in enumerate(data):
        data_to_get[j][2] = i
    showdata(data,all_offest)

def showdata(data,all_offset):
    offset = 5
    half_sizeY = int(round(data[3]/2))

    to_offest = offset
    if all_offset:
        to_offest = half_sizeY
    
    display.cartesian_generation(data[0],data[1],data[2],data[3],data[4],to_offest)
    display.showfunction(data[0],data[1],data[2],data[3],data[4],data[5])

def Main():
    while True:
        ask_data(all_offest)
        print("\n"*5)

if __name__ == "__main__":
    Main()