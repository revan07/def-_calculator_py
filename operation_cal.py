# (def add) is a function that use two parameter for a addition and (str class) to become a parameter in operator
def add(x, y): 
    print(str(x + y))

# (def subtract) is a function that use two parameter for a subtract and (str class) to become a parameter in operator
def subtract(x, y):
    print(str(x - y))

# (def multiply) is a function that use two parameter for a multiply and (str class) to become a parameter in operator
def multiply(x, y):
    print(str(x * y))

# (def divide) is a function that use two parameter for a divide and (str class) to become a parameter in operator
def divide(x, y):
    print(str(x / y))

# (def residual) is a function that use two parameter for a residual and (str class) to become a parameter in operator
def residual(x, y):
    print(str(x % y))

# (def exponentual) is a function that use two parameter for a exponentual and (str class) to become a parameter in operator
def exponentual(x, y):
    print(str(x ** y))


print("welcome at my calculator UwU. Whrite a operator and two number for operate \n\n")

#here create loop while infinite Im use (True) to become while a loop infinite
while True:
    symbol_operator = input("whrite operator: ") # variable (symbol_operator) almacenate valor for console

    if symbol_operator == "+": #(symbol_operator) is validate for if-elif with any operator input for console
        addition1 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        addition2 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        add(addition1, addition2) # here pass the variables in the position of parameters
        
    elif symbol_operator == "-": # variable (symbol_operator) almacenate valor for console
        addition1 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        addition2 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        subtract(addition1, addition2) # here pass the variables in the position of parameters
        
    elif symbol_operator == "*": # variable (symbol_operator) almacenate valor for console
        addition1 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        addition2 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        multiply(addition1, addition2) # here pass the variables in the position of parameters
        
    elif symbol_operator == "/": # variable (symbol_operator) almacenate valor for console
        addition1 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        addition2 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        divide(addition1, addition2) # here pass the variables in the position of parameters
        
    elif symbol_operator == "%": # variable (symbol_operator) almacenate valor for console
        addition1 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        addition2 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        residual(addition1, addition2) # here pass the variables in the position of parameters
        
    elif symbol_operator == "**": # variable (symbol_operator) almacenate valor for console
        addition1 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        addition2 = int(input("whrite one for add operation: ")) # almacenate valor from input for console
        exponentual(addition1, addition2) # here pass the variables in the position of parameters
    
    #here is a condition which validate if (simbol_operator) receibe string "exit". 
    #This make that program closep using (break) to broken code
    elif symbol_operator == "exit": 
        break
