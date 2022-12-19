def getx():
 with open("filex.txt", "r") as file:
    last_line1 = file.readlines()[-1]
    x=float(last_line1)
    return x
def gety():    
 with open("filey.txt", "r") as file:
    last_line2 = file.readlines()[-1]
    y=float(last_line2)
    return y
def getz():    
 with open("filez.txt", "r") as file:
    last_line3 = file.readlines()[-1]
    z=float(last_line3)   
    return z   
