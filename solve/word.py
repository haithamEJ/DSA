
word = str(input())
big = 0 
small = 0

for i in range(0,len(word)):
    if word[i].isupper():
        big = big + 1
    elif word[i].islower():
        small = small + 1

if big > small : 
    new = word.upper() 
    print(new)

if big <= small : 
    new = word.lower()
    print(new)