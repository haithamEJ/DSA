import bcrypt
import pyfiglet 
from termcolor import colored 

def welcome():
    ascii_text2 = pyfiglet.figlet_format("Welcome Haitham !", font="small")
    colored_ascii2 = colored(ascii_text2, "red")

    print(colored_ascii2)


def ask():
     ascii_text2 = pyfiglet.figlet_format("What do u need?", font="small")
     colored_ascii2 = colored(ascii_text2, "yellow")
     print(colored_ascii2)
     print("+ Press 1 if u wanna search a password \n+ Press 2 if u wanna delete a password \n+ Press 3 to update a password \n+ Press 4 to add a password")
     insert = input("Press the number :")

     match insert:
        case "1":
            print("You chose One!")
        case "2":
            print("You chose Two!")
        case "3":
            print("You chose Three!")
        case "4":
            website = input("Enter the website name or the use (1 word only): ")
            password = input("Enter the password")         
            has = hash(password) 
            print(has)

            userPassword =  'password'
            userBytes = userPassword.encode('utf-8') 
            result = bcrypt.checkpw(userBytes, has)   
            print(result)
        case _:
            print("Invalid choice!")



def hash(password):

    bytes = password.encode('utf-8') 
    salt = bcrypt.gensalt() 
    hash = bcrypt.hashpw(bytes, salt) 

    return hash


welcome()
ask()

# with open("D:\\zri3a.txt","a") as f:
#     f.write(f"{has} \n")
# f = open("D:\\zri3a.txt","r")
# print(f.read())