from list7 import ex2, ex3
print("Welcome!")
print("List 7: String exercises")
print("List 8: Tuple exercises")
print("List 9: Dictionary exercises")
ans = int(input("Select a list: "))
match ans:
    case 7:
        print("List 7: String exercises")
        print("[2] Remove unnecessary spaces")
        print("[3] Expand dashes")
        ans = int(input("Select an exercise: "))
        match ans:
            case 2:
                ex2()
            case 3:
                ex3()
            case _:
                print("Invalid exercise")