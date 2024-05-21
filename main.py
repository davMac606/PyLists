from list7 import ex2
print("Welcome!")
print("List 7: String exercises")
print("List 8: Tuple exercises")
print("List 9: Dictionary exercises")
ans = int(input("Select a list: "))
match ans:
    case 7:
        ans = int(input("Select an exercise: "))
        match ans:
            case 2:
                ex2()