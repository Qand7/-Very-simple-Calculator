import os
os.system('cls')
print("Taschenrechner!")
numCounter = 1
validAnswers = ["A", "B", "C", "D", "E"]

def askAction():
    print("\nActions: ")
    act = (input(" A) add \n B) subtract \n C) multiply \n D) divide \n E) calculate  \n\n [A/B/C/D/E]? : ").strip().upper())

    if (act in validAnswers):
        return act
    
    else:
        print("invalid Answer")
        return askAction()
    
def askNumber():
    global numCounter

    try:
        n = int(input(f"\n {numCounter} Number: "))
    except ValueError:
        print("invalid Answer")
        return askNumber()
    else:
        numCounter += 1
        return int(n)

def main():
    x = int(askNumber())
    a = askAction()

    if(a != "E"):
        y = int(askNumber())

        if (a == "A"):
            x += y
        elif (a == "B"):
            x -= y
        elif (a == "C"):
            x *= y
        elif (a == "D"):
            if (y == 0):
                print("Cannot divide by 0")
                y = askNumber()
            else:
                x /= y
        
        a = askAction()

    print("\nResult: ", x, "\n")

        
main()