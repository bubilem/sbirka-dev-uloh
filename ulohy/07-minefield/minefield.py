import random

def generate_field(field:dict)->dict:
    field["grid"] = [[0 for _ in range(field["height"])] for _ in range(field["width"])]
    if field["mines"] > field["width"] * field["height"]:
        field["mines"] = 0
        print("Too many mines.")    
    for _ in range(field["mines"]):
        while True:
            rx = random.randint(0, field["width"] - 1)
            ry = random.randint(0, field["height"] - 1)
            if field["grid"][rx][ry] != "M":
                field["grid"][rx][ry] = "M"
                break
    neighbours = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    for x in range(field["width"]):
        for y in range(field["height"]):
            if field["grid"][x][y] == "M":
                for neighbour in neighbours:
                    nx = x + neighbour[0]
                    ny = y + neighbour[1]
                    if nx >= 0 and nx < field["width"] and ny >= 0 and ny < field["height"]:
                        if field["grid"][nx][ny] != "M":
                            field["grid"][nx][ny] += 1
    return field

def print_field(field:dict):
    RED = '\033[91m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    RESET = '\033[0m'
    for y in range(field["height"]):
        for x in range(field["width"]):
            if field["grid"][x][y] == "M":
                print(RED, end="")
            elif field["grid"][x][y] > 0:
                print(WHITE, end="")
            else:
                print(GRAY, end="")
            print(field["grid"][x][y], RESET, sep="", end="")            
        print()


field = {
    "width": 30,
    "height": 10,
    "mines": 25,
    "grid":[]}

field = generate_field(field)
print_field(field)