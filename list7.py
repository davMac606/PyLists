import os
def ex2():
    print("Exercise 2: Remove unnecessary spaces")
    ans = input("Do you want the version using 'strip' method? (y/n)")
    match ans:
        case 'y':
            s = input("Enter a string: ")
            print(s.strip())
        case 'n':
            s = input("Enter a string: ")
            print(s.replace(" ", ""))
            
def ex3(): 
    print("Exercise 3: Expand dashes")
    s = input("Enter a string: ")
    ind = s.find("-")
    prev = s[ind-1]
    nex = s[ind+1]
    letter = ord(prev)
    while letter <= ord(nex):
        print(chr(letter), end="")
        letter += 1
    
    
    