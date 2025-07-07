from colorama import init, Fore, Style
init(autoreset=True)

def isnum(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    

print(Fore.CYAN +""" 
Welcome to the calculator app!
You can press "q" to quit anytime you want. Have fun.
""")

while True:
    print()

    op = input(Fore.YELLOW +"Choose an operator from the following 4 operators : +  -  /  *  : ")
    if op.lower() == "q":
        print(Fore.GREEN + "Thank you for using the program. GoodBye.")
        break
    n1 = input(Fore.YELLOW +"Enter the first number: ")
    if n1.lower() == "q":
        break
    n2 = input(Fore.YELLOW +"Enter the second number: ")
    if n2.lower() == "q":
        break

    if not (isnum(n1) and isnum(n2)):
        print(Fore.RED + "\nInvalid input please enter numbers.")
        continue

    n1 = float(n1)
    n2 = float(n2)

    if op == "+":
        r =  n1 + n2
    elif op == "-":
        r =  n1 - n2
    elif op == "*":
        r =  n1 * n2
    elif op == "/":
        if n2 == 0:
            print(Fore.RED +"Error: division by zero is not allowed.")
            continue
        else:
            r =  n1 / n2
    else:
        print(Fore.RED + "Invalid operator. Please enter an operator from the 4 alternatives.")
        continue
        
    print(Fore.GREEN + f"Result : {r}")
