import bcrypt 
  
def hash(password):

    bytes = password.encode('utf-8') 
    salt = bcrypt.gensalt() 
    hash = bcrypt.hashpw(bytes, salt) 

    return hash
 
password = 'password'
has = hash(password) 
print(has)
userPassword =  'password'
userBytes = userPassword.encode('utf-8') 
result = bcrypt.checkpw(userBytes, has) 
  
print(result)