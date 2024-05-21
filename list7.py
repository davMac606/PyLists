import os
def ex2():
    ans = input("Do you want the version using 'strip' method? (y/n)")
    match ans:
        case 'y':
            s = input("Enter a string: ")
            print(s.strip())
        case 'n':
            s = input("Enter a string: ")
            print(s.replace(" ", ""))