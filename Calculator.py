result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input("Wait for input: ")
    if wait_for_number and result == None:
        try:
            result = float(user_input)
            wait_for_number = False
        except ValueError:
            print(f"{user_input} is not a number. Try again")

    elif user_input == "=":
        print(f"Your result is {round(result, 2)}")
        break
    
    elif not wait_for_number:
        try:
            if user_input == "+" or\
            user_input == "-" or\
            user_input == "*" or\
            user_input == "/":
                operator = user_input
                wait_for_number = True
            else:
                print(f"{user_input} is not '+' or '-' or '/' or '*'.Try again")
        except ValueError:
            print(f"{user_input} is not an operator. Try again")
        

    elif wait_for_number:
        try:
            operand = float(user_input)
            result = eval(f"{result} {operator} {operand}")
            operand = None
            operator = None
            wait_for_number = False
        except ZeroDivisionError:
            print("You can not divide by zero")
            continue
        except ValueError:
            print(f"{user_input} is not a number. Try again")

            

