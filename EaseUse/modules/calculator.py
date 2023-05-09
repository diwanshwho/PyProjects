def calc():
    import math
    print("You have entered CALCULATOR mode ▼")
    basic = ['+', '-', '*', '/', '//', '%', 'pow']
    advanced = ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', '!', 'asin', 'acos', 'atan']
    print("Available Operations ↓")
    print("Basic--",basic)
    print("Advanced--",advanced)
    oper = input("Kindly provide the operation -→").strip()
    if oper in basic:
        first, second = map(float, input('Provide 2 values (seperated by comma) -→ ').split(','))
        print("Operated Result ↓\n")
        match oper:
            case '+': print(first + second)
            case '-': print(first - second)
            case '*': print(first * second)
            case '/': print(first / second)
            case '//': print(int(first // second))
            case '%': print((first*100)/second)
            case 'pow': print(first ** second)
    if oper in advanced:
        first = float(input('Provide value -→ '))
        print("Operated Result ↓\n")
        match oper:
            case 'sin': print(math.sin(first))
            case 'cos': print(math.cos(first))
            case 'tan': print(math.tan(first))
            case 'log': print(math.log10(first))
            case 'ln': print(math.log(first))
            case 'sqrt': print(math.sqrt(first))
            case '!': print(math.factorial(int(first)))
            case 'asin': print(math.asin(first))
            case 'acos': print(math.acos(first))
            case 'atan': print(math.atan(first))
    else:
        print("How can One be so Wrong!!")
