matrice = []


sizeX = int(input("enter columns"))
sizeY = int(input("enter rows"))


for i in range(sizeX):
    for j in range(sizeY):
        m = i * j
        print(m, end="")
        matrice.append("freaky ")


def check(tab,x,y):
    mat = []
    for i in range(x):
        for j in range(y):
            mat.append(tab[i])
    return mat


test = check(matrice,sizeX,sizeY)
print(test)
