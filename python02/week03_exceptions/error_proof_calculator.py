
def addition(x, y):
    return x + y



def subtraction(x, y):
    return x - y



def multiplication(x, y):
    return x * y



def division(x, y):
    return x / y


def modulo(x, y):
    return x % y



operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '%': modulo
}



def calculate_formula(input_str):

    try:
        numeros = input_str.strip().split()
        
        if len(numeros) != 3:

            raise Exception("Invalid formula. Please provide a valid formula with 3 elements.")
        
        num1, operator, num2 = numeros
        
        num1 = float(num1)
        num2 = float(num2)
        
        if operator not in operators:
            raise Exception("Invalid operator. Please use one of these operators: +, -, *, /, %")
        
        return operators[operator](num1, num2)
    
    
    except ValueError:
        raise Exception("Invalid numbers. Please provide valid numbers for calculation.")
    
    except Exception as e:
        raise Exception("An error occurred during calculation. Please try again.") from e



def main():

    while True:
        try:
            user_input = input("Enter a formula (e.g., 1 + 1) or 'quit' to exit: ").title()
            
            if user_input == 'Quit':
                break
            
            result = calculate_formula(user_input)
            print(f"Result: {result}")
        
        except Exception as e:
            
            print(f"Error: {e}")

main()
