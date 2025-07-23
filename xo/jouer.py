def display(tableB):
    for i in range(0,len(tableB)):
            print("|"+(tableB[i] if tableB[i] != "" else " "), end="")
            if (i+1) % 3 == 0 :
                print("|\n")
    print("\n==============================================")

def insertBoard(position, role):
    if position < 0 or position >= len(gameBoard):
        print("Invalid position. Choose between 1 and 9.")
        return False

    if gameBoard[position] != "":
        print("u cant do this move")
        return False

    gameBoard[position] = role
    display(gameBoard) 


    if check(gameBoard,len(gameBoard)):
        print(f"{role} wins!")
        exit()

    return True

gameBoard = ["","","","","","","","",""]
role = "X"
i = 0

def jouer():
    role = "X"
    counter = 0
    while counter < 9:
        while True:
            try:
                if role == "X":
                    x = int(input("\n Enter the position of X: "))
                    if insertBoard(x - 1, role):
                     role = "O" 
                     counter = counter +1  
                    break  
                if role == "O":
                    y = int(input("\n Enter the position of O: "))
                    if insertBoard(y-1, role):
                     role = "X" 
                     counter = counter +1
                    break  
            except ValueError:
                print("Invalid input. Please enter an integer.")


def check(tab,size):
    checking = []

    for i in range(size):
        checking.append(tab[i])
    
    if (checking[0] == "X" and checking[1] == "X" and checking[2] == "X") or (checking[0] == "O" and checking[1] == "O" and checking[2] == "O") :
        return True
    
    if (checking[3] == "X" and checking[4] == "X" and checking[5] == "X") or (checking[3] == "O" and checking[4] == "O" and checking[5] == "O") :
        return True
    
    if (checking[6] == "X" and checking[7] == "X" and checking[8] == "X") or (checking[6] == "O" and checking[7] == "O" and checking[8] == "O") :
        return True
    
    if (checking[0] == "X" and checking[4] == "X" and checking[8] == "X") or (checking[0] == "O" and checking[4] == "O" and checking[8] == "O") :
        return True
    
    if (checking[2] == "X" and checking[4] == "X" and checking[6] == "X") or (checking[2] == "O" and checking[4] == "O" and checking[6] == "O") :
        return True
    
    else:
        return False

    
jouer()
# 8 combinaisons 
'''
8 combinaisons
1,2,3 (x or o)
4,5,6 (x or o)
7,8,9 (x or o)

1,5,9 (x or o)
3,5,7 (x or o)
'''
print("Game is done !")

